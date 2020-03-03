# Zachary Hayes


def sort_array(the_array):
    the_array.sort()        # No return statement because arrays are passed by reference.


def search_array(the_array, to_search):
    try:
        return the_array.index(to_search)
    except ValueError as err:
        return -1
