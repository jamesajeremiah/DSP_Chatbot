# Author: James Jeremiah
# james2.jeremiah@uwe.ac.uk
# Student number: 17042447
# 27/04/2021
# 
# Find all matching patterns in a string using spaCy

# CUDA 11.1 installed


import create_network


''' DEFINE FUNCTIONS '''

def RemoveRepeatIds(match_ids):
    """ Removes repeating elements in list. """

    output = []
    for x in match_ids:
        if x not in output:
            output.append(x)
            
    return output

def main(message, pattern_ids):
    """ Returns all matching patterns using spaCy given an input string. """

    doc = create_network.nlp(message)
    matches = create_network.matcher(doc)
    matching_pattern_ids = []

    for match_id, start, end in matches:
        # Get the matched span
        matched_span = doc[start:end]
        if match_id in pattern_ids:
            matching_pattern_ids.append(pattern_ids[match_id])
            
    matching_pattern_ids = RemoveRepeatIds(matching_pattern_ids)

    return matching_pattern_ids