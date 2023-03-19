from tkinter import *
import start, rooms

# start.go()

root = Tk()
root.geometry('400x350+750+350')
root.title("Мега КРутая ПРОГА")
def go_main():
    root.destroy()




def hut():
    canvas.delete(labK, but1K, but2K, but3K)
    def go():
        canvas.delete(labH, entryH, butH)
        for i in range(int(Hentry.get())):
            root.geometry('400x350+750+350')
            canvas.config(width=400, height=350)
            Rooms(i)
    root.geometry('350x105+750+350')
    canvas.config(width=350, height=105)
    Hlab = Label(text="Введите количество комнат в квартире:",
                width=350,bg='white', fg='black', wraplength=350,
                font=("Bahnschrift", 14),justify=LEFT)
    Hentry = Entry()  
    Hbut = Button(text="Погнали", width=20, command=go)
    labH = canvas.create_window(-30, 0, anchor=NW, window=Hlab, width=350, height=0)
    entryH = canvas.create_window(110, 25, anchor=NW, window=Hentry, width=200, height=0)  
    butH = canvas.create_window(0, 65, anchor=NW, window=Hbut, width=350, height=40)              


def Rooms(i=0):
    canvas.delete(but1K,but2K,but3K,labK)
    rooms.rooms(i, root, canvas)


canvas = Canvas(bg="white", width=400, height=350)
canvas.pack(anchor=CENTER, expand=1)

lab = Label(text="Выберите вариант помещения:",
            width=400,bg='white', fg='black', wraplength=325,
            font=("Bahnschrift", 14))

labK = canvas.create_window(0, 0, anchor=NW, window=lab, width=400, height=0)

but1 = Button(text="Комната", width=20, command=Rooms)
but2 = Button(text="Квартира", width=20, command=hut)
but3 = Button(text="Многоэтажный дом", width=20, command=go_main)


but1K = canvas.create_window(85, 50, anchor=NW, window=but1, width=230, height=80)
but2K = canvas.create_window(85, 140, anchor=NW, window=but2, width=230, height=80)
but3K = canvas.create_window(85, 230, anchor=NW, window=but3, width=230, height=80)


 
root.mainloop()