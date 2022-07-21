import tkinter.font
from tkinter import *

bgColor = "#E9F3F4"
txtColor = "#140572"

inside = "#F0F7F8"
border = "#C8E6EB"

#update command
def update_prices():
    print(entDiscount.get())


updateWindow = Tk()
updateWindow.title("Price Configure Page")
updateWindow.configure(bg=bgColor)
updateWindow.geometry("450x200")

font = tkinter.font.Font(family="ATC Laurel Book", size=10, slant="italic")
Label(updateWindow, text="Enter Discount : ",font=font, fg=txtColor, bg=bgColor).place(x=10, y=30)

discount =StringVar()
entDiscount = Entry(updateWindow,bg=inside,textvariable=discount,highlightthickness=2,highlightbackground=border,width=50)
entDiscount.place(x=120,y=30)

Button(updateWindow, text='Apply', width=15,fg=txtColor, bg=inside, relief="ridge",
       highlightcolor=border,command=update_prices).place(x=225,y=60)

updateWindow.mainloop()