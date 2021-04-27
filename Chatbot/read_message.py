# Author: James Jeremiah
# james2.jeremiah@uwe.ac.uk
# Student number: 17042447
# 27/04/2021
# 
# Takes the message from a user and returns the best fit response
# This is done by matching patterns using spaCy and navigating through the knowledge graph to the best fit topic
# Once the conversation is over, an email is sent containing the conversation log


import create_network
import find_pattern
import send_ticket


''' DEFINE CONSTANTS '''

PATTERNS = create_network.main()


''' DEFINE CLASSES '''

class conversation():
    """ Conversation class stores information about the conversation. """

    def __init__(self, user_name=None):
        """ Create a new conversation. Its topic will be defined by the user's messages. """

        self.topic = create_network.get_node_by_id("ROOT") # topics are objects
        self.solution = ""
        self.chat_log = ""
        
        # set user name only if given
        if user_name: 
            self.user_name = user_name
        else:
            self.user_name = "unspecified-staff@uwe.ac.uk"
    

    def set_topic(self, id):
        """ Set topic by its ID """

        self.topic = create_network.get_node_by_id(id)
    

    def get_response(self):
        """ Get the topic object's response """

        return self.topic.response


class matcher():
    """ Matcher class stores information about all matching patterns given the user's message. """

    def __init__(self, user_message):
        """ Create a new list of matching patterns. """

        self.patterns = find_pattern.main(user_message, PATTERNS)
        

    def matching_topics(self, topic):
        """ Returns all matching patterns that are also found in the topic's list of children. """

        matched_children = []
        for child in topic.children:
            child_id, child_patterns = child[0], child[1]
            if child_patterns in self.patterns:
                matched_children.append(child_id)
        return matched_children

    def is_resolved(self):
        """ Returns True if the query has been successfully resolved. """

        if "RESOLVED" in self.patterns:
            return True


''' INITIALISE GLOBAL OBJECT '''
current_conversation = conversation()


''' DEFINE FUNCTIONS '''

def find_response(user_message):
    """ Searches through the knowledge graph to find the best fit topic given a user's message.
    Then, returns that topic's response. """

    # Define globals and variables
    global current_conversation
    response = ""
    nodes_travelled = -1 # to track if network has travelled down at least one new topic

    # Create object and match patterns with user's message
    new_matcher = matcher(user_message)

    # Using the matched patterns, navigate through the network until the deepest topic possible is reached
    while(1):
        nodes_travelled += 1

        # If topic has a solution
        if current_conversation.topic.has_solution:

            # If network has just reached a solution
            # Return response and ask if the solution solved their query
            if nodes_travelled > 0:
                response = f"{current_conversation.get_response()}\n\nDid this information solve your query?"
                break

            # If given solution is successful
            # Set to resolution topic, return response and provoke new conversation topic
            elif new_matcher.is_resolved():
                current_conversation.set_topic("RESOLVED")
                response = f"{current_conversation.get_response()}\n\nCan I help you with anything else?"
                break

            # If solution is not successful but alternative solutions exist
            # Go to child topic
            elif current_conversation.topic.children:
                current_conversation.set_topic(current_conversation.topic.children[0][0])

            # Else, there are no more solutions to provide and query is unsolved
            else:
                current_conversation.set_topic("UNSOLVED")
                response = f"{current_conversation.get_response()}\n\nCan I help you with anything else?"
                break

        
        # If topic does not have a solution
        else:
            
            # Store child topics with patterns that match with the user's message
            matching_topics = new_matcher.matching_topics(current_conversation.topic)

            # If exactly 1 matching child, go to that child topic and keep searching
            if len(matching_topics) == 1:
                current_conversation.set_topic(matching_topics[0])
            
            # If more than one matching child, ask the user which problem they are having
            # If the conversation has just started, prioritise the first matching pattern
            elif len(matching_topics) > 1:
                if current_conversation.topic.id == "ROOT":
                    current_conversation.set_topic(matching_topics[0])
                else:    
                    response = f"{current_conversation.topic.response}\n\nCould you clarify if this is this a problem with:"
                    for child in matching_topics:
                        response += f"\n\n{child}"
                    break
            
            # If no topics matched
            # Return its repsonse if the topic has changed with the user's message
            # Otherwise ask for clarification
            elif len(matching_topics) == 0:
                if nodes_travelled > 0:
                    response = f"{current_conversation.topic.response}"
                else:
                    response = f"Sorry, I didn't recognise what you meant. I have knowledge about these topics:"
                    for child in current_conversation.topic.children:
                        response += f"\n\n{child[0]}"
                    
                break

    return response


def main(user_message):
    """ Receives string input from messenger platform and returns a response.
    If the query has been resolved, send a ticket to ITOnline. """

    global current_conversation
    
    response = find_response(user_message)

    # Append message and response to chat log
    current_conversation.chat_log += f"\n\n{current_conversation.user_name}:\n{user_message}\n\nCHATBOT:\n{response}"
    
    # If solution topic reached, set it
    if current_conversation.topic.has_solution:
        current_conversation.solution = current_conversation.topic.id

    # If a resolution has been reached
    # Send ticket and start new conversation
    elif current_conversation.topic.is_resolution:    
        send_ticket.main(current_conversation)
        current_conversation = conversation(current_conversation.user_name)
        
    # Send response message to user    
    return response


if __name__ == "__main__":
    main()