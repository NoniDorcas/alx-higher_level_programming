#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list.copy()

    if idx is < 0 or >= len(my_list):
        return new

    new[idx] = element
    return new
