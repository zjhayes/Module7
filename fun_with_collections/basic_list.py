# Zachary Hayes


def make_list():
    list_size = 3
    list = [list_size]
    for i in range(list_size):
        list[i] = get_input()
    return list



def get_input():
    pass



if __name__ == '__main__':
    try:  # check for ValueError
        make_list()

    except ValueError as err:
        print("ValueError encountered!")