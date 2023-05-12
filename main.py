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


def is_my_path_included(path_1, path_2) :
    delete_path_1 =  delete_path_2 =False
    if path_1.find(path_2)  :
        delete_path_1 = True
    if path_2.find(path_1) :
        delete_path_2 = True
    return(delete_path_1,delete_path_2)




# 1 #Quel type de fichier- loop ajouter un chemin
#* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
paths_to_check =  ['C:/Users/altji/Pictures','C:/Users/altji/Documents/Guild Wars 2','C:/Users/altji/Pictures/toto','C:/Users/altji/Pictures/pingouin']
# i=0
# while 0 <= i:
#     from tkinter.filedialog import askdirectory
#     paths_to_check.append( askdirectory( title='Select Folder')) # shows dialog box and return the path
#     if paths_to_check[i] =='' :
#         del paths_to_check[i]
#         print(paths_to_check)
#         break
#     else :
#         i+=1


#verif sur le fait que les chemins ne sont pas inclus l un dans l autre

for  indexX in range(0, len(paths_to_check)-1) :
    print(f"checking {paths_to_check[indexX]}")
    for indexY in range(indexX+1, len(paths_to_check)) :
            print(f"checking {paths_to_check[indexX]} and {paths_to_check[indexY]}")

            if is_my_path_included(paths_to_check[indexX],paths_to_check[indexY]) == (True, True):
                print("true, true")
                #paths_to_check.remove(indexY)
                #paths_to_check.pop(indexY)
                #del paths_to_check[indexX]

            # if is_my_path_included(paths_to_check[indexX],paths_to_check[indexY]) ==(False, True):
            #     # del paths_to_check[indexY]
            #     print("False, true")
            # if is_my_path_included(paths_to_check[indexX],paths_to_check[indexY]) ==(True, False):
            #     # paths_to_check.remove(indexX)
            #     print("true, False")
            indexY=+1
    indexX=indexX+1

print(paths_to_check)
#===============================================================




# 2 ajouter une verif sur le fait que les chemins ne sont pas inclus l un dans l autre
#* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

#===============================================================



# 3 quel types de doublons on cherche
#* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

typefichier= ['.jpg',".png",".jpeg"]
# typefichier= []
#
# user_answer = 2 #input("quel type de fichier : 1 pour son, 2 pour video, 3 pour image, 4 pour pdf. Taper le choix :")
#
# if user_answer == 1 :
#     typefichier = ('.wav','.mp3', '.aac','.aiff','.flac', ".m4a")
# elif  user_answer == 2 :
#     typefichier = ('.mp4','.mov','.avi','.mkv')
# else  :
#     exit
#===============================================================


all_files_to_compare  = {}


# 3 lister les fichiers
#* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
special_i = 0
for path in paths_to_check :
    #print(f'path we are testing {path}')
    #print(special_i)
    for root, dirs, files in os.walk(path):
        for file in files:
            #print(f'     file we are testing {os.path.join(file)}')
            if compare_extensions(os.path.join(file), typefichier) == True  :
                all_files_to_compare[special_i] ={'path_w_file' : os.path.abspath(root), 'filename':os.path.join(file),"extension":os.path.splitext(file)[-1].lower()}
                special_i=special_i+1
                print(f"found files {os.path.join(root,file)}")


#pour verifier si j ai pete un truc decommenter en dessous :
#print(all_files_to_compare)
#===============================================================



# #    4 verifier les doublons de noms
# #toto = "Capture.png" in  all_files_to_compare.keys()
# print('jusque la tout va bien')
for id in all_files_to_compare :
    File_in_work = str.lower(all_files_to_compare[id]['filename'])
    #print(File_in_work)
    for y in range(id+1, len(all_files_to_compare.keys())) :
        #print(y)
        #print(all_files_to_compare[y]['filename'])
        if str.lower(all_files_to_compare[y]['filename'])==File_in_work :
            print(f"its a match ! the file {File_in_work} in {all_files_to_compare[id]['path_w_file']}  is a double of {all_files_to_compare[y]['filename']} in {all_files_to_compare[y]['path_w_file']}" )
   # print(File_in_work)

#


