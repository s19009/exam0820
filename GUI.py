from tkinter import Tk, Text, Button, Entry
from tkinter import messagebox as mb


root = Tk()
root.title('あなたの名前は？')

text = Entry(root)
text.pack()


def say_hello():
    a = text.get()
    mb.showinfo('挨拶', a + 'さんこんにちは')


button = Button(
    text="教える",
    width=10, height=3,
    command=say_hello
)
button.pack()

root.mainloop()
