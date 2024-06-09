import tkinter as tk
from tkinter import ttk
from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt
import ex

v = []


class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder=None):
        super().__init__(master)

        if placeholder is not None:
            self.placeholder = placeholder
            self.placeholder_color = "grey"
            self.default_fg_color = self["fg"]

            self.bind("<FocusIn>", self.focus_in)
            self.bind("<FocusOut>", self.focus_out)

            self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self["fg"] = self.placeholder_color

    def focus_in(self, *args):
        if self["fg"] == self.placeholder_color:
            self.delete("0", "end")
            self["fg"] = self.default_fg_color

    def focus_out(self, *args):
        if not self.get():
            self.put_placeholder()


def get_value_e():

    pass


def switch_windows():
    window1.withdraw()
    window2.deiconify()


def get_value_v():
    global G, pos, value
    value = int(ent_v.get())
    G = nx.MultiGraph()

    for i in range(value):
        G.add_node(
            i,
        )

    # pos = nx.get_node_attributes(G, 'pos')
    # pos = nx.circular_layout(G)
    pos = ex.get_points(1, value)

    # pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True)

    # v = v[::-1]
    # nx.draw(G, pos, with_labels=True)
    # print(G.nodes(data=True))
    plt.show()


def name_v():
    node = int(ent_e_1.get())
    text = ent_e_2.get()
    a = pos[node][0] + 0.1
    b = pos[node][1] + 0.1
    pos[node] = (a, b)

    nx.draw_networkx_labels(G, pos, {node: text})


global pokaz
pokaz = []


def get_value_pokaz():

    value_pokaz = int(ent_pokaz.get())
    for i in range(value_pokaz):
        string = f"п{i+1}"
        pokaz.append(string)

    n = tk.StringVar()
    combobox = ttk.Combobox(window2, width=27, textvariable=n)
    combobox["values"] = pokaz
    combobox.place(relx=0.014, rely=0.40)
    combobox.current()

    ent_for_combobox = Entry(window2)
    ent_for_combobox.place(relx=0.014, rely=0.45)

    def create_pokaz():

        pokazatel = combobox.get()
        name = ent_for_combobox.get()
        arr = []
        arr.append(pokazatel)
        arr.append(name)

        global pokaz
        pokaz.append(arr)

    btn_for_combobox = Button(window2, text="Создать показатель", command=create_pokaz)
    btn_for_combobox.place(relx=0.25, rely=0.45)

    def show_pokaz():
        label_for_show_pokaz = Label(
            window2,
            text=f"{pokaz[3][0]}->{pokaz[3][1]}\n{pokaz[4][0]}->{pokaz[4][1]}\n{pokaz[5][0]}->{pokaz[5][1]}",
        )
        label_for_show_pokaz.place(relx=0.45, rely=0.50)

    btn_for_combobox_list = Button(window2, text="Показать все", command=show_pokaz)
    btn_for_combobox_list.place(relx=0.45, rely=0.45)


# def printer():
#     print(pokaz[3:])
#     pass


window1 = Tk()
window1.title("Добро пожаловать!")
window1.geometry("600x400")

lbl = Label(window1, text="Добро пожаловать!")
button = Button(window1, text="Далее", command=switch_windows)

lbl.place(relx=0.4, rely=0.5)
button.place(relx=0.44, rely=0.9)

window2 = tk.Toplevel()
window2.withdraw()
window2.geometry("700x500")

#  //--------------------Создание вершин--------------------\\
label_for_create_v = Label(window2, text="Ввести количество вершин")
label_for_create_v.place(relx=0.01, rely=0.01)

ent_v = Entry(window2)
ent_v.place(relx=0.014, rely=0.06)

btn_for_input_v = Button(window2, text="Ввести количество вершин", command=get_value_v)
btn_for_input_v.place(relx=0.014, rely=0.11)

#  //--------------------Создание параметров--------------------\\

label_for_create_pokaz = Label(window2, text="Ввести количество показателей")
label_for_create_pokaz.place(relx=0.01, rely=0.20)

ent_pokaz = Entry(window2)
ent_pokaz.place(relx=0.014, rely=0.25)

btn_for_input_pokaz = Button(
    window2, text="Ввести количество показателей", command=get_value_pokaz
)
btn_for_input_pokaz.place(relx=0.014, rely=0.30)

#  //--------------------Добавление названий вершинам--------------------\\
label_for_create_e = Label(window2, text="Название вершин")
label_for_create_e.place(relx=0.01, rely=0.50)
ent_e_1 = EntryWithPlaceholder(window2, "Номер вершины")
ent_e_2 = EntryWithPlaceholder(window2, "Название вершины")
ent_e_1.place(relx=0.014, rely=0.55)
ent_e_2.place(relx=0.014, rely=0.60)
btn_for_input_e = Button(window2, text="Добавить", command=name_v)
btn_for_input_e.place(relx=0.014, rely=0.65)

#  //--------------------Создание связей--------------------\\


    

# btn_test = Button(window2, text="test", command=printer)
# btn_test.place(relx=0.014, rely=0.70)

window1.mainloop()


# nx.draw_networkx_labels(G, pos)
