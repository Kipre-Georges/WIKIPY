import wikipedia 
from email.mime import image
from multiprocessing.sharedctypes import Value
from tkinter import*
import random
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk


def action():
    theme=recherche.get()
    wikisearch=wikipedia.page(theme,auto_suggest=False)
    result_research.delete('1.0', END)
    result_research.insert(END, wikisearch.summary)



def ressetButton():
    recherche.delete(0,END)
    result_research.delete(0,END)


wiki = Tk()
wiki.geometry("1920x1080")




Valider=Button(wiki,text="Lancer la recherche",command=action)
Valider.pack
Valider.place(x=10,y=900)


resetButton = Button(wiki,text="Réinitialiser",command=ressetButton)
resetButton.pack()
resetButton.place(x=960,y=900)


quitter= Button(wiki,text="Quitter l'application",command=wiki.destroy)
quitter.pack()
quitter.place(x=1790,y=900)


name_research=Label(wiki,text="Entrez votre recherche : ")
name_research.pack()
name_research.place(x=670,y=100)


recherche=Entry(wiki)
recherche.pack()
recherche.place(x=800,y=100)


result_research = Text(wiki, width=100, height=20)
result_research.place(x=500,y=250)





wiki.mainloop()