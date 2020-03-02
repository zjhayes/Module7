# Zachary Hayes


def make_list():
    list_size = 3
    list = []
    for i in range(list_size):
        list.insert(i, int(get_input()))
    return list


def get_input():
    return input("Enter number: ")


if __name__ == '__main__':
    try:  # check for ValueError
        print(make_list())

    except ValueError as err:
        print("ValueError encountered!")