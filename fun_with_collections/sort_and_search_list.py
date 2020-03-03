#Zachary Hayes

import fun_with_collections.basic_list_exception as topic1


def sort_list():
    list_to_sort = topic1.make_list()
    list_to_sort.sort()         # Did not include return statement because lists are passed by reference.


def search_list(item):
    list_to_search = topic1.make_list()
    try:
        return list_to_search.index(item)
    except ValueError as err:
        return -1
