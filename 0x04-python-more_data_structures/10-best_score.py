#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        max_value = max(a_dictionary.keys())
    else:
        return None
    return max_value
