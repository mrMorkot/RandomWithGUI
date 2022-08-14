from tkinter import *
import tkinter
import random
from tkinter import messagebox

list = ['Java Script', 'Python', 'Blender','Go', 'SQL', 'Поиграй в игру', 'Git', 'HTML/CSS']
def clicked():
    btn['text'] = f'Сегодня занимаешься:\n {random.choice(list)}'

window = tkinter.Tk()
window.title("Генератор учебы")
window['bg'] = 'blue'

label = tkinter.Label(window, text = 'Нажми кнопочку!', bg='blue', fg='red', font= ('Arial Bold', 20) )
label.pack()
window.geometry('400x300+400+300')

btn = tkinter.Button(window, text="Жмяк", bg="blue", fg="yellow", width=50, height=30,
                     font=('Arial Bold', 22), command=clicked )

btn.place(relx=.5, rely=.5, anchor="c", height=210, width=350, bordermode=OUTSIDE)
window.mainloop()



