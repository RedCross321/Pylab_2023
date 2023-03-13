from tkinter import *
import start, apart

# start.go()

root = Tk()
root.geometry('400x350+750+350')
root.title("Мега КРутая ПРОГА")
def go_main():
    root.destroy()




# def hut():
#     count = 0
#     def schet():
#         canvas.delete(labH,entryH,butH)
#         canvas.config(width=400, height=350)
#         root.geometry('400x350+750+350')
#         for _ in range(int(Hentry.get())):
#             apartment()
#         print(tokens)
#     canvas.delete(labK, but1K, but2K, but3K)
#     root.geometry('350x105+750+350')
#     canvas.config(width=350, height=105)
#     Hlab = Label(text="Введите количество комнат в квартире:",
#                 width=350,bg='white', fg='black', wraplength=350,
#                 font=("Bahnschrift", 14),justify=LEFT)
#     Hentry = Entry()  
#     Hbut = Button(text="Погнали", width=20, command=schet)
#     labH = canvas.create_window(-30, 0, anchor=NW, window=Hlab, width=350, height=0)
#     entryH = canvas.create_window(110, 25, anchor=NW, window=Hentry, width=200, height=0)  
#     butH = canvas.create_window(0, 65, anchor=NW, window=Hbut, width=350, height=40)              
#     # for _ in range():


def rooms():
    canvas.delete(but1K,but2K,but3K,labK)
    apart.apartment(root,canvas)


canvas = Canvas(bg="white", width=400, height=350)
canvas.pack(anchor=CENTER, expand=1)

lab = Label(text="Выберите вариант помещения:",
            width=400,bg='white', fg='black', wraplength=325,
            font=("Bahnschrift", 14))

labK = canvas.create_window(0, 0, anchor=NW, window=lab, width=400, height=0)

but1 = Button(text="Комната", width=20, command=rooms)
but2 = Button(text="Квартира", width=20, command=apart.apartment)
but3 = Button(text="Многоэтажный дом", width=20, command=go_main)


but1K = canvas.create_window(85, 50, anchor=NW, window=but1, width=230, height=80)
but2K = canvas.create_window(85, 140, anchor=NW, window=but2, width=230, height=80)
but3K = canvas.create_window(85, 230, anchor=NW, window=but3, width=230, height=80)


 
root.mainloop()