from tkinter.messagebox import *
import os

#===============================================================
# * * * * * * * * * * * F O N C T I O N S * * * * * * * * * * *
#===============================================================


def compare_extensions(file_name, list_of_extensions):

    extension = os.path.splitext(file_name)[-1].lower()
    for x in list_of_extensions:
        if x == extension:
            return True
        else:
            continue


def compare_extensions(file_name, list_of_extensions):

    extension = os.path.splitext(file_name)[-1].lower()
    for x in list_of_extensions:
        if x == extension:
            return True
        else:
            continue


def is_my_path_included(path_1, path_2):
    delete_path_1 = delete_path_2 = False
    if path_1 in path_2:
        delete_path_1 = True
    if path_2 in path_1:
        delete_path_2 = True
    return delete_path_1, delete_path_2





def are_my_paths_redondant_v2(paths_to_check):
    """"takes a list of strings as entry, return the list modified"""

    if len(paths_to_check) == 1:
        return paths_to_check
    index_x = 0
    while index_x in range(0, len(paths_to_check)):
        index_y: int = index_x+1
        while index_y in range(index_x+1, len(paths_to_check)):
            if is_my_path_included(paths_to_check[index_x], paths_to_check[index_y]) == (True, False):
                showinfo("info : ", str(paths_to_check[index_y]) + "\n is included in \n" + str(paths_to_check[index_x]) + " and was deleted.\n")
                del paths_to_check[index_y]
                index_y = index_x

            if is_my_path_included(paths_to_check[index_x], paths_to_check[index_y]) == (False, True):
                showinfo("info : ", str(paths_to_check[index_x]) + "\n is included in \n" + str(paths_to_check[index_y]) + " and was deleted.\n")
                del paths_to_check[index_x]
                break
            index_y = index_y+1
        index_x = index_x+1


    return paths_to_check
