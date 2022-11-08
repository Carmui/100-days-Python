import tkinter
import turtle

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width = 500, height= 300)

#Label

my_label = tkinter.Label(text="I am a Label", font = ("Arial", 24, "italic"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button


def button_clicked():
    newtxt = input.get()
    my_label.config(text=newtxt)


#Entry

input = tkinter.Entry(width=10)
input.pack()


button = tkinter.Button(text="Click me!", command=button_clicked)
button.pack()




window.mainloop()
