import os


#===============================================================
# * * * * * * * * * * * F O N C T I O N S * * * * * * * * * * *
#===============================================================
def compare_extensions(file_name, List_of_extensions) :

    extension = os.path.splitext(file_name)[-1].lower()
    x=0
    for x in (0, len(List_of_extensions)-1) :
        if List_of_extensions[x]== extension :
            return(True)
        else :
            continue





# 1 #Quel type de fichier- loop ajouter un chemin
#* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
paths_to_check =  ['C:/Users/altji/Pictures']
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

#===============================================================




# 2 ajouter une verif sur le fait que les chemins ne sont pas inclus l un dans l autre
#* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

#===============================================================



# 3 quel types de doublons on cherche
#* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

typefichier= ['jpg',"png"]
# typefichier= []
#
# user_answer = 2 #input("quel type de fichier : 1 pour son, 2 pour video, 3 pour image, 4 pour pdf. Taper le choix :")
#
# if user_answer == 1 :
#     typefichier = ['.wav','.mp3', '.aac','.aiff','.flac', ".m4a"]
# elif  user_answer == 2 :
#     typefichier = ['.mp4','.mov','.avi','.mkv' ]
# else  :
#     exit
#===============================================================




# 3 lister les fichiers
#* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
for j in (0, len(paths_to_check)-1) :
    for root, dirs, files in os.walk(paths_to_check[j]):
        print ('loop1',paths_to_check[j], root, dirs, files)
        #faut debugger ici !
        for file in files:
            if compare_extensions(os.path.join(file), typefichier) == True  :
                 print (os.path.join(root)," | ", os.path.join(file) )




