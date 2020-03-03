# Zachary Hayes

def average_scores(*args, **kwargs):
    gpa = calculate_average_score(*args)
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
    return 'Result: name = ' + kwargs['first_name'] + ' gpa = ' + str(gpa) + ' major = ' + kwargs['major']


def calculate_average_score(*args):
    running_total = 0
    running_count = 0
    for arg in args:
        running_total += arg
        running_count += 1
    return running_total / running_count


if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, first_name='Michelle', last_name='Ruse', major='World_domination'))
    print(average_scores(2, 2, 3, 4, first_name='Wade', last_name='Sidie', major='Carpentry'))
    print(average_scores(4, 4, 4, 4, first_name='Zachary', last_name='Hayes', major='Business Information Systems'))




#'Result: name = M gpa = 3.2 course = Python with current average 30.0
