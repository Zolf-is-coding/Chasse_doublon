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


def is_my_path_included(path_1, path_2) :
    delete_path_1 =  delete_path_2 =False
    if path_1 in path_2  :
        delete_path_1 = True
    if path_2 in path_1 :
        delete_path_2 = True
    return(delete_path_1,delete_path_2)


def are_my_paths_redondant(paths_to_check):
    # verif sur le fait que les chemins ne sont pas inclus l un dans l autre
    '''on prend la longueur de la liste
    indexX = l index de la valeur droite a comparer
    indexY = l index de la valeur gauche a comparer, il sera toujours au moins superieur de 1 a indexX

    on bouclera pour arriver a l avant derniere valeur du tableau par indexX
        tant qu on a indexY syperieur a indexX et jusqua la derniere valeur du tableau
        on va comparer le contenu des cles pour la premiere valeur de X
            si le chemin de droite est contenu dans le chemin de gauche, alors on supprime la valeur associee a indexX , et on sort de la boucle car la valeur de droite change.
            si la chemin de gauche est contenu dans le chemin de droite, alors on supprime le contenu de la valeur associe a indexY et on remet la valeur de indexY = indexX car la fin de la boucle le fera incrementa indexX+1 le debut de la boucle
        dans tous les cas, on increment indexY
    '''

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
                    errordetected+= str(paths_to_check[indexY]) +" in included in " + str(paths_to_check[indexX])+ "and was deleted.\n"
                    del paths_to_check[indexY]
                    indexY=indexX

                if is_my_path_included(paths_to_check[indexX],paths_to_check[indexY]) ==(False, True):
                    # print("True, False")
                    errordetected+= str(paths_to_check[indexX]) +" in included in " + str(paths_to_check[indexY])+ "and was deleted.\n"
                    del paths_to_check[indexX]
                    # print("False, True")
                    indexY=indexY+1
                    break
                indexY=indexY+1
        indexX=indexX+1
        # print(f"la valeur de len(paths_to_check)-1 est {len(paths_to_check)-1} et la valeur de indexX est {indexX}")
        # print(paths_to_check)
        # print()
    if errordetected =="" :
        errordetected = "No error detectedd"

   # print(paths_to_check)
    return(paths_to_check,errordetected)



def is_my_path_included_already(paths_to_check, newpath):
    if len(paths_to_check)==0 :
            return(newpath)
    indexX = 0
    addpath=True
    while indexX in range(0, len(paths_to_check)) :
        if is_my_path_included(paths_to_check[indexX],newpath) == (True, False):
            # print("True, False")
            #showinfo("info", f"{newpath}  is included in  {str(paths_to_check[indexX])}and was deleted.\n")
            break

        if is_my_path_included(paths_to_check[indexX],newpath) ==(False, True):
            # print("True, False")
            paths_to_check[indexX] = newpath
            addpath = False
            indexX = newpath
            break

        indexX=indexX+1

    if addpath == True :
        paths_to_check.append(newpath)

   # print(paths_to_check)

    return(paths_to_check)
