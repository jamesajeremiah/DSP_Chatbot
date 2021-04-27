# Author: James Jeremiah
# james2.jeremiah@uwe.ac.uk
# Student number: 17042447
# 27/04/2021
# 
# Creates objects out of all of the topics defined in define_topics.py
# Then define their relationships to one another to form a knowledge graph
# Also defines patterns using spaCy and stores them to match later

import define_topics

import sys

import spacy
from spacy.matcher import Matcher
from spacy.strings import StringStore

spacy.prefer_gpu()
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

list_of_nodes = []
pattern_ids = []
stringstore = []


''' DEFINE GENERIC NODES AND PATTERNS
These nodes will serve as the start and end nodes of each conversation. '''

generic_nodes = [  
(
    # ID
"ROOT",

[   # PATTERNS
],

[   # PARENTS AND PATTERN CONNECTIONS
],

    # RESPONSE
'''Sorry, I'm not sure I recognise that problem. Could you explain your query again, please?''',

    # IS SOLUTION?
False
),


(
    # ID
"RESOLVED",

[   # PATTERNS
[{'LEMMA': 'yes'}],
[{'LEMMA': 'yep'}],
[{'LEMMA': 'yeah'}],
[{'LEMMA': 'solve'}],
],

[   # PARENTS AND PATTERN CONNECTIONS
],

    # RESPONSE
'''I'm glad! I'll send a ticket regarding your resolved query now.\nYou should receive an email confirming this shortly.''',

    # IS SOLUTION?
False
),


(
    # ID
"UNSOLVED",

[   # PATTERNS
[{'LEMMA': 'no'}],
[{'LEMMA': 'nope'}],
[{'LEMMA': 'not'}],
],

[   # PARENTS AND PATTERN CONNECTIONS
],

    # RESPONSE
'''I'm sorry I couldn't help. I'll send a ticket to a human analyst who will help solve your problem.\nYou should receive an email confirming this shortly.''',

    # IS SOLUTION?
False
)

]


''' DEFINE CLASSES '''

class node():
    """ Node class represents a given topic for the chatbot to respond to and how to navigate to other topics. """

    def __init__(self, id, patterns, parents, response, has_solution, is_resolution=False):
        self.id = id
        self.patterns = patterns
        self.response = response
        self.parents = parents
        self.children = [] # Define children seperately so that each node doesn't use the same variable
        self.has_solution = has_solution
        self.is_resolution = is_resolution # Determines if the conversation is over

    def add_child(self, child_id, child_patterns):
        self.children.append([child_id, child_patterns])
    

''' DEFINE FUNCTIONS '''

def get_node_by_id(node_id):
    """ Returns an object by its ID. """

    node = next((node for node in list_of_nodes if node.id == node_id), None) 
    return node


def get_patterns(node_id):
    """ Returns a node's patterns by ID. """

    return get_node_by_id(node_id).patterns


def create_node(id, patterns, parents, response, has_solution):   
    """ Creates node as an object and stores it in a list.
    Also creates the patterns with spaCy and stores its id in a list. """

    # Define and store parent-to-child patterns
    for parent in parents:
        temp_patterns = []
        for ptc_patterns in parent[1]: # parent-to-child patterns
            if isinstance(ptc_patterns, str) == True:                
                temp_patterns += get_patterns(ptc_patterns)
            else:
                temp_patterns.append(ptc_patterns)            
        
        ptc_patterns_id = parent[0] + "_TO_" + id 
        
        matcher.add(ptc_patterns_id, temp_patterns + patterns)
        pattern_ids.append(ptc_patterns_id)
        
        parent[1] = ptc_patterns_id

    node_object = node(id, patterns, parents, response, has_solution) 
    list_of_nodes.append(node_object)
    matcher.add(id, patterns)
    pattern_ids.append(id)


def define_children(list_of_nodes):
    """ Defines the children of each node given the parents of each node.
    This will set up the connections between each node. """

    # Check each node in the network
    # If the node has parents, find it and add the child node to its list of children
    for child_node in list_of_nodes:
        if child_node.parents:
            for parent in child_node.parents:
                parent_id, parent_connections = parent[0], parent[1] # Define for readability
                parent_node = get_node_by_id(parent_id)
                parent_node.add_child(child_node.id, parent_connections)


def create_nodes(nodes):
    """ Creates a list of nodes as objects. """

    for id, patterns, parents, response, has_solution in nodes:
        create_node(id, patterns, parents, response, has_solution)


def define_generic_nodes(generic_nodes):
    """ Create generic nodes (defined at the top) as objects
    Then define their connections to the appropriate nodes. """

    # Get generic nodes 'RESOLVED' and 'UNSOLVED'
    resolved_node = get_node_by_id("RESOLVED")
    unsolved_node = get_node_by_id("UNSOLVED")
    
    # Set RESOLVED, UNSOLVED nodes to be resolution nodes
    resolved_node.is_resolution = True
    unsolved_node.is_resolution = True            

    # Get generic node 'ROOT'
    root_node = get_node_by_id("ROOT")
    
    # Add all non-resolution nodes as children of ROOT
    for node in list_of_nodes:
        if not (node.is_resolution):
            root_node.add_child(node.id, node.id)
        

def main():
    """ Create nodes into objects from the topics defined by administrators.
    Then create the connections between them. """

    nodes = define_topics.main()
    create_nodes(generic_nodes)
    create_nodes(nodes)
    define_children(list_of_nodes)
    define_generic_nodes(generic_nodes)
    stringstore = StringStore(pattern_ids)
    
    return stringstore

if __name__ == "__main__":
    main()