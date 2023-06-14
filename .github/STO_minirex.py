import tkinter as tk
from tkinter import *

listoftupples = ['1', '2','3']

def show_all_doubles(list_to_show):
    photo = PhotoImage(file=r"C:\Users\altji\PycharmProjects\Chasse_doublon\image-sources\delete_by_IYAICON.png")
    """ This fonction takes the List_of_double from the verifier-mes-doublons fonction as its entry"""
    for i in range(0, len(list_to_show)):

        button_left = tk.Button(master=fen1, image=photo, width=32, height=32, command=None)
        button_left.grid(row=8 + i, column=0)

        label1 = tk.Label(master=fen1, text=f"{list_to_show[i]}")
        label1.grid(row=8 + i, column=1)




fen1 = Tk()
fen1.geometry("800x800")


tex1 = Label(fen1, text='this button works with an image', fg='red')
tex1.grid(row=1, column=1, padx=5, pady=5)

photo = PhotoImage(file=r"C:\Users\altji\PycharmProjects\Chasse_doublon\image-sources\delete_by_IYAICON.png")


button_lefttest = tk.Button(master=fen1, image=photo, width=32, height=32, command=None)
button_lefttest.grid(row=1, column=3)


# ligne 6
bouton_check_my_paths = Button(fen1, text='Verifier mes doublons : ', command=show_all_doubles(listoftupples))
bouton_check_my_paths.grid(row=6, column=1, padx=5, pady=5)

fen1.mainloop()


