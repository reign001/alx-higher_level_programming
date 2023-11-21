#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
   """print x elements of a list.
   Args:
   my_list[list]: the list to print element from.
   x(int): the number of element of my_list to print.
   Return:
   the number of element to be printef. """
    num = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            num += 1
        except IndexError:
            break
    print("")
    Return (num)

