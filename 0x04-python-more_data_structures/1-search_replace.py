#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)

    return new_list
original_list = [1, 2, 3, 4, 2, 5, 2]
search_value = 2
replace_value = 9

result_list = search_replace(original_list, search_value, replace_value)
print(result_list)

