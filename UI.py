import tkinter as tk
from tkinter import filedialog
from tkinter import *
from my_fonctions import are_my_paths_redondant


def update_paths_visible_for_user ():
    global globalpath
    global Liste_chemins_lisibles
    Liste_chemins_lisibles = ""
    for element in globalpath :
        Liste_chemins_lisibles =Liste_chemins_lisibles + element + "\n "

    lbl_variable_content.config(text=Liste_chemins_lisibles, anchor='w')

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    filename = filedialog.askdirectory()
    global globalpath
    globalpath.append(filename)
    update_paths_visible_for_user()
    return


def bouton_verification():
    global globalpath
    So_many_errors=""
    paths_To_check,So_many_errors = are_my_paths_redondant(globalpath)
    lbl_error_content.config(text=So_many_errors, anchor='w')
    globalpath = paths_To_check
    lbl_variable_content.config(text=Liste_chemins_lisibles, anchor='w')
    update_paths_visible_for_user()
    return()



######## I N I T I A L I S A T I O N   D E   L A     F E N E T R E #########
fen1 = Tk()
fen1.geometry("800x800")


## I N I T I A L I S A T I O N   D E S    V A R I A B L E S  #########
############      G L O B A L E S     #############
globalpath = []

Liste_chemins_lisibles = ''




########### D E B U T    D U   C O D E ####
tex1 = Label(fen1, text='Bonjour tout le monde !', fg='red')
tex1.grid(row=1, column=1, padx=5, pady=5)


#ligne 2
tex1 = Label(fen1, text='cliquer ici pour ajouter un chemin', fg='red')
tex1.grid(row=2, column=1, padx=5, pady=5)
bou1 = Button(fen1, text='ajouter', command = browse_button)
bou1.grid(row=2,column=2, padx=5, pady=5)


lbl_spacer = tk.Label(fen1, text="")
lbl_spacer.grid(row=3, column=5, sticky="e", padx=5, pady=5)



#ligne 4
lbl_your_selected_paths = tk.Label(fen1, text=f'vos chemins sont :')
lbl_your_selected_paths.grid(row=4, column=1, sticky="e", padx=5, pady=5)

lbl_variable_content = tk.Label(fen1, text=Liste_chemins_lisibles, anchor='w')
lbl_variable_content.grid(row=4, column=2, sticky="e", padx=5, pady=5)



lbl_spacer = tk.Label(fen1, text="")
lbl_spacer.grid(row=5, column=5, sticky="e", padx=5, pady=5)


#ligne 6
bouton_check_my_paths = Button(fen1, text='Verifier mes chemins : ', command = bouton_verification)
bouton_check_my_paths.grid(row=6,column=1, padx=5, pady=5)


lbl_error_content = tk.Label(fen1, text='', anchor='w')
lbl_error_content.grid(row=6, column=2, sticky="e", padx=5, pady=5)


lbl_spacer = tk.Label(fen1, text="")
lbl_spacer.grid(row=7, column=5, sticky="e", padx=5, pady=5)

button_check_my_doubles = Button(fen1, text='Verifier mes doublons  : ', command = bouton_verification)
button_check_my_doubles.grid(row=6,column=1, padx=5, pady=5)

fen1.mainloop()