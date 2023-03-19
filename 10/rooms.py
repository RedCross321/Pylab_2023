from tkinter import *
from tkinter import ttk
import schet

def rooms(i,root,canvas):
    root1 = Tk()
    root1.geometry('400x375+750+350')
    root1.title(f'Комната {i+1}')
    def spravka():
        def kon():
            spravochka.destroy()
        spravochka = Tk()
        spravochka.geometry('550x400+750+350')
        spravochka.title("СПРАВКА!")
        lab0 = Label(spravochka,text="К = 3,0 - 4,0 - Деревянная конструкция или конструкция из гофрированного металлического листа.\n К = 2,0 - 2,9  - Здание с одинарной кирпичной кладкой, упрощенная конструкция окон и крыши.\n К = 1,0 - 1,9 - Стандартная конструкция.\n Двойная кирпичная кладка, крыша со стандартной кровлей, небольшое кол-во окон.\n К = 0,6 - 0,9 - Кирпичные стены с двойной теплоизоляцией, небольшое кол-во окон со сдвоенными рамами, толстое основание пола, крыша из высококачественного теплоизоляционного материала.\n Чем хуже теплоизоляция, тем больший коэффициент нужно выбирать.  ", 
                     width=550,bg='white', fg='black', wraplength=550, font=("Bahnschrift", 14),justify=LEFT)
        lab0.pack()
        but0 = Button(spravochka, text="Понял!", width=70, command=kon, height=40)
        but0.pack()
        spravochka.mainloop()
    def Schet():
        root1.destroy()
        # canvas.delete(lab1K, lab2K, lab3K, lab4K, lab5K, lab6K, lab7K, but11K, but22K, entry1K, entry2K, entry3K, entry4K, entry5K, entry6K)
        root.geometry('450x150+750+350')
        x, y = schet.gigachad(float(entry1.get()), float(entry2.get()), float(entry3.get()), float(entry4.get()), float(entry5.get()), float(entry6.get()))
        lab11 = Label(root,text=f'Площадь помещения: {x} м^2\n\nТепловая мощность для обогрева: {y} кВт',
        width=450,bg='white', fg='black', wraplength=450, font=("Bahnschrift", 14),justify=LEFT)
        # butt = Button(root,text="Конец(", width=20, command=vixod)
        # canvas.create_window(120, 95, anchor=NW, window=butt, width=200, height=50)
        canvas.create_window(-30, 0, anchor=NW, window=lab11, width=350, height=0)
        lab11.pack()
        # butt.pack()
        # canvas.create_window(-20, 0, anchor=NW, window=lab11, width=450, height=0)


    lab1 = Label(root1, anchor=N, text="Заполните данные о комнате", width=400,bg='white', fg='black', wraplength=325, font=("Bahnschrift", 14))
    lab2 = Label(root1,anchor=W,text="Ширина комнаты:", width=400,bg='white', fg='black', wraplength=225, font=("Bahnschrift", 14))
    lab3 = Label(root1, anchor=W,text="Длина комнаты:", width=400,bg='white', fg='black', wraplength=325, font=("Bahnschrift", 14))
    lab4 = Label(root1, anchor=W,text="Высота комнаты:", width=400,bg='white', fg='black', wraplength=325, font=("Bahnschrift", 14))   
    lab5 = Label(root1, anchor=W,text="Коэффициент тепловых потерь:", width=400,bg='white', fg='black', wraplength=325, font=("Bahnschrift", 14))
    lab6 = Label(root1, anchor=W,text="Температура в квартире:", width=400,bg='white', fg='black', wraplength=325, font=("Bahnschrift", 14)) 
    lab7 = Label(root1, anchor=W,text="Температура за окном:", width=400,bg='white', fg='black', wraplength=325, font=("Bahnschrift", 14))
    but1 = Button(root1, text="Справка", width=20, command=spravka)
    but2 = Button(root1, text="Вычислить", width=25, command=Schet)
    entry1 = Entry(root1,width=400)
    entry2 = Entry(root1,width=400)
    entry3 = Entry(root1,width=400)
    entry4 = Entry(root1,width=400)
    entry5 = Entry(root1,width=400)
    entry6 = Entry(root1,width=400)

    
    lab1.pack()
    lab2.pack()
    entry1.pack(anchor=W)
    lab3.pack()
    entry2.pack(anchor=W)
    lab4.pack()
    entry3.pack(anchor=W)
    lab5.pack()
    entry4.pack(anchor=W)
    lab6.pack()
    entry5.pack(anchor=W)
    lab7.pack()
    entry6.pack(anchor=W)
    but1.pack(side = LEFT, fill=Y)
    but2.pack(side=RIGHT, fill=Y)
    # lab1K = canvas.create_window(0, 0, anchor=NW, window=lab1, width=400, height=0)
    # lab2K = canvas.create_window(90, 30, anchor=N, window=lab2, width=400, height=0)
    # entry1K = canvas.create_window(180, 33, anchor=NW, window=entry1, width=200, height=0)

    # # lab3K = canvas.create_window(90, 60, anchor=N, window=lab3, width=400, height=0)
    # entry2K = canvas.create_window(180, 63, anchor=NW, window=entry2, width=200, height=0)



    # # lab4K = canvas.create_window(90, 90, anchor=N, window=lab4, width=400, height=0)
    # entry3K = canvas.create_window(180, 93, anchor=NW, window=entry3, width=200, height=0)



    # # lab5K = canvas.create_window(165, 120, anchor=N, window=lab5, width=400, height=0)
    # entry4K = canvas.create_window(5, 150, anchor=NW, window=entry4, width=200, height=0)
    # but11K = canvas.create_window(210, 147, anchor=NW, window=but1, width=170, height=0)


    # # lab6K = canvas.create_window(130, 180, anchor=N, window=lab6, width=400, height=0)
    # entry5K = canvas.create_window(260, 183, anchor=NW, window=entry5, width=120, height=0)



    # # lab7K = canvas.create_window(120, 210, anchor=N, window=lab7, width=400, height=0)
    # entry6K = canvas.create_window(240, 213, anchor=NW, window=entry6, width=140, height=0)
    # but22K = canvas.create_window(115, 260, anchor=NW, window=but2, width=170, height=60)