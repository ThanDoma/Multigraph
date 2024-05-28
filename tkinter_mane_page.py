from tkinter import *
import tkinter as tk
from create_graph import create

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder=None):
        super().__init__(master)

        if placeholder is not None:
            self.placeholder = placeholder
            self.placeholder_color = 'grey'
            self.default_fg_color = self['fg']

            self.bind("<FocusIn>", self.focus_in)
            self.bind("<FocusOut>", self.focus_out)

            self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def focus_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def focus_out(self, *args):
        if not self.get():
            self.put_placeholder()

v1_v2_e = []

def kol_vo_v ():
    global kol_v
    kol_v = int(text_filed_v.get())
    
def create_e ():
    global v1, v2, e
    v1 = int(text_filed_v1.get())
    v2 = int(text_filed_v2.get())
    e = int(text_filed_e.get())
    comd = [v1, v2, e]
    v1_v2_e.append(comd)
        
    
def create_g ():
    create(v1_v2_e, kol_v)

# Создаём главное окно приложения
root = Tk()
root.title("Моё приложение")
root.geometry('600x400')

# Создаём надпись
label_kol_v = Label(root, text="Введите количество вершин: ")
label_create = Label(root, text="Создание связей между вершинами")

# Создаём текстовое поле
text_filed_v = EntryWithPlaceholder(root, )
text_filed_v1 = EntryWithPlaceholder(root, 'Вершина 1') 
text_filed_v2 = EntryWithPlaceholder(root, 'Вершина 2')
text_filed_e = EntryWithPlaceholder(root, 'Вес')

# Создаём кнопку
btn_add_v = Button(root, text="Добавить", command=kol_vo_v)
btn_create = Button(root, text="Создать связь", command=create_e)
btn_create_graph = Button(root, text="Создать граф", command=create_g)

label_kol_v.pack()
text_filed_v.pack()
btn_add_v.pack()

label_create.pack()
text_filed_v1.pack()
text_filed_v2.pack()
text_filed_e.pack()

btn_create.pack()
btn_create_graph.pack()


# Запускаем главный цикл окна
root.mainloop()

