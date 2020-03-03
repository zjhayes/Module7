# Zachary Hayes
import array as arr


def sort_array(the_array):
    sorted_list = the_array.tolist().sort()
    sorted_array = arr.array('d', sorted_list)
    return sorted_array
    # I used a return because even though arrays are passed by reference, I had to convert it to a list because
    # apparently arrays don't have sort.


def search_array(the_array, to_search):
    try:
        return the_array.index(to_search)
    except ValueError as err:
        return -1
