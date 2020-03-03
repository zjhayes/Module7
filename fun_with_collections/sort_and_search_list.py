#Zachary Hayes

import fun_with_collections.basic_list_exception as topic1


def sort_list():
    list_to_sort = topic1.make_list()
    list_to_sort.sort()
    return list_to_sort
    # Even though list is passed by reference, I had to return it to use it in my test since the input was mocked.


def search_list(item):
    list_to_search = topic1.make_list()
    try:
        return list_to_search.index(item)
    except ValueError as err:
        return -1
