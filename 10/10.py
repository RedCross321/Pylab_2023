from tkinter import *
from tkinter import ttk
import room


root = Tk()
root.geometry('1200x850')
root.title("Мега КРутая ПРОГА")
ttk.Label(text="Длина помещения в м3").place(x=100, y=20)
ttk.Label(text="Ширина помещения в м3").place(x=100, y=50)
ttk.Label(text="Высота помещения в м3").place(x=100, y=80)
ttk.Label(text="Температура воздуха вне помещения в °С").place(x=100, y=110)
ttk.Label(text="Температура воздуха в помещения в °С").place(x=100, y=140)
ttk.Label(text="Коэффициент тепловых потерь").place(x=100, y=170)
ttk.Label(text="Сколько комнат в этой квартире").place(x=700, y=200)
ttk.Label(text="Сколько квартир в этом доме").place(x=700, y=230)
ttk.Label(text="РЕЗУЛЬТАТЫ ПОДСЧЕТОВ").place(x=800, y=300)
ttk.Label(text="Общая площадь помещения:").place(x=700, y=330)
ttk.Label(text="Тепловой мощности для обогрева помещения(кВт):").place(x=700, y=360)
spr_jpeg = PhotoImage(file="ppp.png")
Spr = ttk.Label(image=spr_jpeg, text="Справка для определения коэффициента", compound="top")
Spr.place(x=100, y=200)

RezS = ttk.Label()
RezP = ttk.Label()
RezS.place(x=920, y=330)
RezP.place(x=1070, y=360)

Elength = ttk.Entry(width=50)
Elength.place(x=700, y=20)

Ewidth = ttk.Entry(width=50)
Ewidth.place(x=700, y=50)

Eheight = ttk.Entry(width=50)
Eheight.place(x=700, y=80)

Etemp1 = ttk.Entry(width=50)
Etemp1.place(x=700, y=110)

Etemp2 = ttk.Entry(width=50)
Etemp2.place(x=700, y=140)

Ekof = ttk.Entry(width=50)
Ekof.place(x=700, y=170)

Rooms = ttk.Entry(width=20)
Rooms.place(x=900, y=200)

Apartmens = ttk.Entry(width=20)
Apartmens.place(x=900, y=230)

N = 0

def cpcp():
    N = int(Rooms.get())
    Elength.delete(0, END)
    Ewidth.delete(0, END)
    Eheight.delete(0, END)
    Etemp1.delete(0, END)
    Etemp2.delete(0, END)
    Ekof.delete(0, END)

def pcpc():
    N = int(Apartmens.get())
    Elength.delete(0, END)
    Ewidth.delete(0, END)
    Eheight.delete(0, END)
    Etemp1.delete(0, END)
    Etemp2.delete(0, END)
    Ekof.delete(0, END)


def click_button():
    RezS["text"], RezP["text"] = room.schet(float(Elength.get()), float(Ewidth.get()), float(Eheight.get()), int(Etemp1.get()),int(Etemp2.get()),float(Ekof.get()))

btn = ttk.Button(text="Посчитать", command=click_button)
btn.place(x=700, y=400)

btn1 = ttk.Button(text="ок", command=cpcp)
btn1.place(x=1100, y=200)

btn2 = ttk.Button(text="окей", command=pcpc)
btn2.place(x=1100, y=230)

root.mainloop()
