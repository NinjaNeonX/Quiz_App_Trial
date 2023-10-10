import tkinter
from tkinter import messagebox
import time

#creating and setting window
window = tkinter.Tk()

window.title("Quiz")
window.iconbitmap("img/icon/icon.ico")
window.configure(bg = "white")
window.geometry("1800x1000")

#variable
time1 = ''
clock = tkinter.Label(window, font=('times', 40, 'bold'), bg='white')
clock.place(x=1150, y=430)
logo_photo = tkinter.PhotoImage(file = "img/icon/logo.png")
logo = tkinter.Label(window, image = logo_photo, bg = "white").place(x=1095, y=90)


ans = tkinter.StringVar()



#main
def statusvar():

	tkinter.Label(window, text="Welcome to Quiz", borderwidth=8, relief=tkinter.GROOVE, font="Forte 16 bold", padx=2200,pady=6).pack()


def buttons():

	Play_with_computer = tkinter.Button(window, text = "  Play with computer  ", font="Forte 16 bold", command = category1).place(x = 650, y = 300)
	Play_with_Friend = tkinter.Button(window, text = "Play with Friends", font="Forte 16 bold").place(x = 670, y = 250)
	Offline_Games = tkinter.Button(window, text = "Offline Games", font="Forte 16 bold").place(x = 680, y = 350)
	rules_about = tkinter.Button(window, text = "  Rules and About  ", font="Forte 16 bold", command = rules_and_about).place(x = 660, y = 400)
	EXIT = tkinter.Button(window, text = "    Exit     ", font="Forte 16 bold", command = window.quit, bg = "red").place(x = 700, y = 450)




#Game definetion
def snakegame():
	import snake_game


def mazegame():
	import mazegame


def ttt():

	import ttt


#clock definition
def tick():
    global time1

    time2 = time.strftime('%H:%M:%S')

    if time2 != time1:
        time1 = time2
        clock.config(text=time2)

    clock.after(200, tick)

#function definitions
def offline_games():

	win3 = tkinter.Tk()
	win3.configure(bg = "white")
	win3.title("Quiz")
	win3.iconbitmap("img/icon/icon.ico")
	win3.geometry("300x200")
	win3.maxsize(width = 300, height = 200)
	win3.minsize(width = 300, height = 200)

	tkinter.Button(win3, text = "Tic Tac Toe Game", font="Forte 16 bold", command = ttt).pack(pady = 12)
	tkinter.Button(win3, text = "Maze Game", font="Forte 16 bold", command = mazegame).pack(pady = 14)
	tkinter.Button(win3, text = "Snake Game", font="Forte 16 bold", command = snakegame).pack()


def category1():
	win1 = tkinter.Tk()
	win1.configure(bg = "white")
	win1.title("Quiz")
	win1.iconbitmap("img/icon/icon.ico")
	win1.geometry("200x150")

	Math = tkinter.Button(win1, text = "Math", font="Forte 16 bold").pack(pady = 12)
	Simple_Quiz = tkinter.Button(win1, text = "Simple Quiz", font="Forte 16 bold").pack()



def about():

	win6 = tkinter.Tk()
	win6.iconbitmap("img/icon/icon.ico")
	win6.title("Quiz")
	win6.configure(bg = "white")
	win6.geometry("1050x500")
	win6.maxsize(width = 1050, height = 500)
	win6.minsize(width = 1050, height = 500)

	abt_text = '''This is a Quiz app made just for adults but the quiz contants some easy question too,

	if you can solve all the question then you will know everything about math,

	science and other subjects and the intresting thing is there will be more levels coming soon....'''

	tkinter.Label(win6, text = abt_text, font ="Timenewromans 16 bold", bg = "white").pack()


def rules():

	win5 = tkinter.Tk()
	win5.configure(bg = "white")
	win5.title("Quiz")
	win5.iconbitmap("img/icon/icon.ico")
	win5.geometry("500x400")

	tkinter.Button(win5, text = "Rules for 'Play with computer' ", font ="Forte 16 bold").pack(pady = 16)
	tkinter.Button(win5, text = "Rules for 'Play with Friends' ", font ="Forte 16 bold").pack(pady = 16)
	tkinter.Button(win5, text = "Rules for 'Offline Games' ", font ="Forte 16 bold").pack(pady = 16)



def rules_and_about():

	win4 = tkinter.Tk()
	win4.configure(bg = "white")
	win4.title("Quiz")
	win4.iconbitmap("img/icon/icon.ico")
	win4.geometry("200x170")

	tkinter.Button(win4, text = "Rules", font="Forte 16 bold", command = rules).pack(pady = 12)
	tkinter.Button(win4, text = "About", font="Forte 16 bold", command = about).pack(pady = 12)





tick()
statusvar()
buttons()
window_image = tkinter.PhotoImage(file = "img/BG/BG.png")
tkinter.Label(window, image = window_image, borderwidth = 0).place(x = 600, y = 100)
window.mainloop()