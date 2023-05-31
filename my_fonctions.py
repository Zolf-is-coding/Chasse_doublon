from tkinter.messagebox import *
import os

#===============================================================
# * * * * * * * * * * * F O N C T I O N S * * * * * * * * * * *
#===============================================================
def compare_extensions(file_name, List_of_extensions) :

    extension = os.path.splitext(file_name)[-1].lower()
    for x in (List_of_extensions) :
        if x == extension :
            return(True)
        else :
            continue
def compare_extensions(file_name, List_of_extensions) :

    extension = os.path.splitext(file_name)[-1].lower()
    for x in (List_of_extensions) :
        if x == extension :
            return(True)
        else :
            continue


def is_my_path_included(path_1, path_2) :
    delete_path_1 =  delete_path_2 =False
    if path_1 in path_2  :
        delete_path_1 = True
    if path_2 in path_1 :
        delete_path_2 = True
    return(delete_path_1,delete_path_2)





def are_my_paths_redondant_v2(paths_to_check):

    if len(paths_to_check)==1 :
            return(paths_to_check)
    indexX = 0
    errordetected = ""
    while indexX in range(0, len(paths_to_check)) :
       # print(f"checking {paths_to_check[indexX]}")
        indexY: int=indexX+1
        while indexY in range(indexX+1, len(paths_to_check)) :
                #print(f"checking {paths_to_check[indexX]} and {paths_to_check[indexY]}")
                # print(f" indexX = {indexX} et indexY = {indexY}")
                # print(len(paths_to_check))
                if is_my_path_included(paths_to_check[indexX],paths_to_check[indexY]) == (True, False):
                    # print("True, False")
                    showinfo( "info", str(paths_to_check[indexY]) +"\n is included in \n" + str(paths_to_check[indexX])+ " and was deleted.\n")
                    del paths_to_check[indexY]
                    indexY=indexX

                if is_my_path_included(paths_to_check[indexX],paths_to_check[indexY]) ==(False, True):

                    showinfo( "info",str(paths_to_check[indexX]) +"\n is included in \n" + str(paths_to_check[indexY])+ " and was deleted.\n")
                    del paths_to_check[indexX]
                    break
                indexY=indexY+1
        indexX=indexX+1


   # print(paths_to_check)
    return(paths_to_check)


