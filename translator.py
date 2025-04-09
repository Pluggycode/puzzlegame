from tkinter import * 
from tkinter import messagebox,ttk
import googletrans
import textblob

root = Tk()
root.title("Language Translator")
root.geometry("1080x400")
# icon
image_icon =PhotoImage(file = "ai1.png")
root.iconphoto(False, image_icon)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

cobol = ttk.Combobox(root, values= languageV, font='Roboto 14', state='r')
cobol.place(x=20, y=20)
cobol.set('english')
label1 = Label(root, text="Enter Text", font='Roboto 14', bg='white',width=40,bd=5,relief=GROOVE).place(x=20, y=50)
f = Frame(root, bg='black', bd=5).place(x=20, y=90, width=440, height=210)

text1 = Text(f, font='Roboto 14',bg='light yellow',relief=GROOVE, wrap=WORD).place(x=25, y=95, width=430, height=200)

cobol2 = ttk.Combobox(root, values= languageV, font='Roboto 14', state='r')
cobol2.place(x=600, y=20)
cobol2.set('select language')
label1 = Label(root, text="Enter Text", font='Roboto 14', bg='white',width=40,bd=5,relief=GROOVE).place(x=600, y=50)
f = Frame(root, bg='white', bd=5).place(x=600, y=90, width=440, height=210)

Scrollbar1 = Scrollbar(f)
Scrollbar1.pack(side='right', fill=Y)
Scrollbar1.config(command=text1.yview)
text1.config(yscrollcommand=Scrollbar1.set)


root.configure(bg = 'light blue')
root.mainloop()
