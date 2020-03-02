# Zachary Hayes


def make_list():
    list_size = 3
    list = []
    for i in range(list_size):
        user_input = int(get_input())
        if user_input <= 0 or user_input > 100:
            raise ValueError
        list.insert(i, user_input)
    return list


def get_input():
    return input("Enter number: ")


if __name__ == '__main__':
    try:  # check for ValueError
        print(make_list())

    except ValueError as err:
        print("ValueError encountered!")