from tkinter import Tk, Text, Button, Entry
from tkinter import messagebox as mb
import datetime


root = Tk()
root.title('あなたの名前は？')
root.geometry("500x300")

text = Entry(width=30)
text.place(x=125, y=100)

time = datetime.datetime.now()


def say_hello():
    a = text.get()
    if time.hour <= 10:
        mb.showinfo('挨拶', a + 'さんおはようございます')
    elif time.hour >= 18:
        mb.showinfo('挨拶', a + 'さんこんばんは')
    else:
        mb.showinfo('挨拶', a + 'さんこんにちは')


button = Button(
    text="教える",
    width=10, height=2,
    command=say_hello
)
button.place(x=200, y=200)

root.mainloop()
