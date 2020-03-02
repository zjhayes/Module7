#Zachary Hayes


def sort_list(list_to_sort):
    list_to_sort.sort()         # Did not include return statement because lists are passed by reference.


def search_list(list_to_search, item):
    try:
        return list_to_search.index(item)
    except ValueError as err:
        return -1


if __name__ == '__main__':
    try:  # check for ValueError
        the_list = [5,3,2]
        print(search_list(the_list, 3))
        print(the_list)
    except ValueError as err:
        print("ValueError encountered!")