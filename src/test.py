import tkinter as tk
from tkinter import filedialog
from tkinter import *
from my_fonctions import compare_extensions
from my_fonctions import are_my_paths_redondant_v2
import os


def update_paths_visible_for_user():
    global globalpath
    global liste_chemins_lisibles
    liste_chemins_lisibles = ""
    for element in globalpath:
        liste_chemins_lisibles = liste_chemins_lisibles + element + "\n "

    lbl_variable_content.config(text=liste_chemins_lisibles, anchor='w')


def browse_button_v2():
    global globalpath
    globalpath.append(filedialog.askdirectory())
    globalpath = are_my_paths_redondant_v2(globalpath)
    update_paths_visible_for_user()
    return


def boutton_verifier_mes_doublons():
    global globalpath
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    special_i = 0
    for path in globalpath:
        print(path)
        for root, dirs, files in os.walk(path):
            for file in files:
                if compare_extensions(os.path.join(file), typefichier):
                    all_files_to_compare[special_i] = {'path_w_file': os.path.abspath(root),
                                                       'path_wo_file': os.path.dirname(file),
                                                       'filename': os.path.join(file),
                                                       'extension': os.path.splitext(file)[-1].lower()}

                    special_i = special_i + 1

    list_of_my_doubles = []

    for id in all_files_to_compare:
        file_in_work = str.lower(all_files_to_compare[id]['filename'])
        for y in range(id + 1, len(all_files_to_compare.keys())):
            if str.lower(all_files_to_compare[y]['filename']) == file_in_work:
                print(
                    f"its a match ! the file {file_in_work} in {all_files_to_compare[id]['path_w_file']}  is a double of {all_files_to_compare[y]['filename']} in {all_files_to_compare[y]['path_w_file']}")
                temp_tupple = (all_files_to_compare[y]['path_w_file'], all_files_to_compare[y]['filename'],
                               all_files_to_compare[id]['path_w_file'], all_files_to_compare[id]['filename'])
                list_of_my_doubles.append(temp_tupple)


        show_all_doubles(list_of_my_doubles)




def show_all_doubles(list_to_show):
    """ This fonction takes the List_of_double from the verifier-mes-doublons fonction as its entry"""
    for i in range(0, len(list_to_show)):

        label0 = tk.Label(master=fen1, text=f"ins boutton delete")
        label0.grid(row=8 + i, column=0)

        label1 = tk.Label(master=fen1, text=f"{list_to_show[i][0]}")
        label1.grid(row=8 + i, column=1)

        label2 = tk.Label(master=fen1, text=f"{list_to_show[i][1]}")
        label2.grid(row=8 + i, column=2)

        label3 = tk.Label(master=fen1, text=f"{list_to_show[i][2]}")
        label3.grid(row=8 + i, column=3)

        label4 = tk.Label(master=fen1, text=f"{list_to_show[i][3]}")
        label4.grid(row=8 + i, column=4)

        label5 = tk.Label(master=fen1, text=f"ins boutton delete")
        label5.grid(row=8 + i, column=5)


# ####### I N I T I A L I S A T I O N   D E   L A     F E N E T R E #########
fen1 = Tk()
fen1.geometry("800x800")

## I N I T I A L I S A T I O N   D E S    V A R I A B L E S  #########

globalpath = []  # !! THIS ONE IS GLOBAL

liste_chemins_lisibles = ''
all_files_to_compare = {}


##assignet vairable for easier testing
typefichier = ['.jpg', ".png", ".jpeg"]
# globalpath = ['C:/Users/altji/Pictures']

########### D E B U T    D U   C O D E ####
tex1 = Label(fen1, text='Bonjour tout le monde !', fg='red')
tex1.grid(row=1, column=1, padx=5, pady=5)

# ligne 2
tex1 = Label(fen1, text='cliquer ici pour ajouter un chemin', fg='red')
tex1.grid(row=2, column=1, padx=5, pady=5)
bou1 = Button(fen1, text='ajouter', command=browse_button_v2)
bou1.grid(row=2, column=2, padx=5, pady=5)

lbl_spacer = tk.Label(fen1, text="")
lbl_spacer.grid(row=3, column=5, sticky="e", padx=5, pady=5)

# ligne 4
lbl_your_selected_paths = tk.Label(fen1, text=f'vos chemins sont :')
lbl_your_selected_paths.grid(row=4, column=1, sticky="e", padx=5, pady=5)

lbl_variable_content = tk.Label(fen1, text=liste_chemins_lisibles, anchor='w')
lbl_variable_content.grid(row=4, column=2, sticky="e", padx=5, pady=5)

lbl_spacer = tk.Label(fen1, text="")
lbl_spacer.grid(row=5, column=5, sticky="e", padx=5, pady=5)

# ligne 6
bouton_check_my_paths = Button(fen1, text='Verifier mes doublons : ', command=boutton_verifier_mes_doublons)
bouton_check_my_paths.grid(row=6, column=1, padx=5, pady=5)

lbl_error_content = tk.Label(fen1, text='', anchor='w')
lbl_error_content.grid(row=6, column=2, sticky="e", padx=5, pady=5)

lbl_spacer = tk.Label(fen1, text="")
lbl_spacer.grid(row=7, column=5, sticky="e", padx=5, pady=5)

# List_of_my_doubles = [('toto','c/toto','toto2','c/toto2'),('toto','c/toto','toto2','c/toto2')]


fen1.mainloop()

####  F O N C T I O N S ######
