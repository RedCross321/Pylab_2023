from tkinter import *

def go():
    def go_main():
        root.destroy()
    root = Tk()
    root.title("Мега КРутая ПРОГА")
    root.geometry('350x330+750+350')

    canvas = Canvas(bg="white", width=350, height=330)
    canvas.pack(anchor=CENTER, expand=1)

    logo = PhotoImage(file="4.png")
    lab = Label(image = logo, text="Программа для рассчета общей площади и тепловой мощности для обогрева помещения",
                width=400,bg='white', fg='black', wraplength=325, compound='top',
                font=("Bahnschrift", 14))
    but = Button(text="Начать", width=20, command=go_main)


    canvas.create_window(-25, 0, anchor=NW, window=lab, width=400, height=300)
    canvas.create_window(110, 290, anchor=NW, window=but, width=130, height=30)
    root.mainloop()
