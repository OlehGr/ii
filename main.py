import os
import sys
import tkinter as tk
#from barcode import main_bar
from tkinter.ttk import Style

from barcode import main_bar
from face_rec import face_comparison
from frame import save_face
from tkinter import *
from qr_code import qr
import requests

list_product = {'4602041005196':'Кукурузики', '4600494695650':'Энергетик'}
id = {2:"Олег", 4:"Максим", 5:"Артем"}
photo_id = {"oleg.png":"Олег", "maks.jpg":"Максим", "artem.png":"Артем"}
window = tk.Tk()
window.geometry('600x400+200+100')
window.title("Target Hunter")
window.configure(bg='navy')
# window.attributes("-fullscreen", True)

style = Style()

style.configure('W.TButton',
                          font = ('arial', 20, 'bold', ''),
                        foreground = 'red')


def close_window():
    window.attributes("-fullscreen", False)



def click_one_b():
    try:
        os.makedirs("frame")
    except:
        pass
    for a, b in list_product.items():
        if a in main_bar():
            s1 = tk.Label(text=b, anchor='w').pack(fill='both', padx=20)

def buy():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def click_qr_b():
    qr()
    qr_button.destroy()
    face_button.destroy()
    user_id = tk.Label(text="Артём")
    user_id.pack(anchor=NE)
    tk.Button(text="Сканировать", width=15, height=2, bg="gray", fg="black", command=click_one_b).pack()
    tk.Button(text="Купить", width=15, height=2, bg="gray", fg="black", command=buy).pack()
    tk.Label(text="Название:", anchor='w').pack(fill='both', padx=20, pady=20)

def click_face_b():
    try:
        os.makedirs("frame")
    except:
        pass
    save_face()
    result = face_comparison()
    if result[0] == True:
        qr_button.destroy()
        face_button.destroy()
        for a, b in photo_id.items():
            if a == result[1]:
                user_id = tk.Label(text=b)
                for c,d in id.items():
                    if b == d:
                        list_cat = ""
                        r = requests.get(f'https://shop.kulpinov.site/api/v1/docs/prefer?user_id={c}')
                        for i in r.json():
                            list_cat += f" {i['category']['name']}"
                        tk.Label(text=f"Рекомендации  покупке: {list_cat}").pack()
                break
        user_id.pack(anchor=NE)

        tk.Button(text="Сканировать", width=15, height=2, bg="gray", fg="black", command=click_one_b).pack()
        tk.Button(text="Купить", width=15, height=2, bg="gray", fg="black", command=buy).pack()
        tk.Label(text="Корзина товаров:", anchor='w').pack(fill='both', padx=20, pady=20)

qr_button = tk.Button(
                        text="Войти по qr",
                        command=click_qr_b,
                        font=('arial', 20, 'bold'),
                        borderwidth=0,
                        width=27,
                        height=3,
                        bg="deepskyblue",
                        fg="white",
)
qr_button.place(relx=.5, rely=.3, anchor=CENTER)
face_button = tk.Button(
                        command=click_face_b,
                        text="Войти по биометрии",
                        font=('arial', 20, 'bold'),
                        borderwidth=0,
                        width=27,
                        height=3,
                        bg="deepskyblue",
                        fg="white",
)
face_button.place(relx=.5, rely=.65, anchor=CENTER)


window.mainloop()