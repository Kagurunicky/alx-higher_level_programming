#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = sorted(a_dictionary.keys())
    for keys in new:
        print(f"{keys}: {a_dictionary[keys]}")
    return new
