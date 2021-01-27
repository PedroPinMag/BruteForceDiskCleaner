from tkinter import *
import shutil


def myClick():
    while True:
        arquivo.writelines("string")

total, used, free = shutil.disk_usage("/")

arquivo = open('txt.txt', 'w')
pedro = Tk()
pedro.iconbitmap("ico.ico")
pedro.geometry("300x300")
pedro.title("Disk Cleaner")

mylabel = Label(pedro, text="Erase All?")
mylabel.pack()

myButton = Button(pedro, text="Yes!", command=myClick)
myButton.pack()

mylabel2 = Label(pedro, text="If the program stop working just leave it running")
mylabel2.pack()

mylabel4 = Label(pedro,text="\n")
mylabel4.pack()

mylabel5 = Label(pedro, text="When your Disk becomes Full just delete\n the file txt.txt and delete it ")
mylabel5.pack()

mylabel6 = Label(pedro, text="Repeat this process many times")
mylabel6.pack()

pedro.mainloop()
