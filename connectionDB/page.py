import database
import tkinter.font
from tkinter import *
from tkinter import ttk, IntVar
import database
from functools import partial

bgColor = "#E9F3F4"
txtColor = "#140572"

inside= "#F0F7F8"
border = "#C8E6EB"

mainPage = Tk()

#eksik yapılamadı
def select_item(event):
    event = table.focus()
    print(table.item(event))

    updadeButton.configure(state=NORMAL)
    deleteButton.configure(state=NORMAL)


def open_new_window():
    updateWindow = Toplevel(mainPage)
    updateWindow.title("Price Configure Page")
    updateWindow.configure(bg=bgColor)
    updateWindow.geometry("450x200")

    font = tkinter.font.Font(family="ATC Laurel Book", size=10, slant="italic")
    Label(updateWindow, text="Enter Discount : ", font=font, fg=txtColor, bg=bgColor).place(x=10, y=30)

    discount = StringVar()
    entDiscount = Entry(updateWindow, bg=inside, textvariable=discount, highlightthickness=2,
                        highlightbackground=border, width=50)
    entDiscount.place(x=120, y=30)

    Button(updateWindow, text='Apply', width=15, fg=txtColor, bg=inside, relief="ridge",
           highlightcolor=border, command=update_prices).place(x=225, y=60)

    updateWindow.mainloop()
    return entDiscount.get()


# select xcommand
def get_All(table):
    for i in database.select():
        table.insert(parent='', index='end', iid=i, text='',values=(i))
    updadeButton.configure(state=NORMAL)
    deleteButton.configure(state=NORMAL)


def get_condition():
    database.select_with_conditions(entSearch.get())

def update_prices():
    print("updated")

#insert command
def add_book():
    print("added")


#delete command
def delete_book():
    #kitbı buraya geçirmeye çalış
    print("deleted")




titleFont = tkinter.font.Font(family="ATC Laurel Book",size=25,weight="bold",slant="italic")

lbTitle = Label(mainPage,text="The Cozy Book Store", font=titleFont, pady=20, fg=txtColor,bg=bgColor)
lbTitle.place(x=350,y=40,anchor="center")

#entery height ayarla
condition = StringVar()
entSearch = Entry(mainPage, textvariable=condition, bg=inside, highlightthickness=2, highlightbackground=border, width=50)
entSearch.place(x=40,y=90)


table_frame = Frame(mainPage)
table_frame.pack()

table = ttk.Treeview(table_frame)

table['columns'] = ('ISBN', 'Book name', 'Writer', 'Publisher', 'Price', 'Page', 'Score')

table.column("#0", width=0, stretch=NO)
table.column("ISBN", anchor=CENTER, width=80)
table.column("Book name", anchor=CENTER, width=80)
table.column("Writer", anchor=CENTER, width=80)
table.column("Publisher", anchor=CENTER, width=80)
table.column("Price", anchor=CENTER, width=80)
table.column("Page", anchor=CENTER, width=80)
table.column("Score", anchor=CENTER, width=80)

table.heading("#0", text="", anchor=CENTER)
table.heading("ISBN", text="ISBN", anchor=CENTER)
table.heading("Book name", text="Book name", anchor=CENTER)
table.heading("Writer", text="Writer", anchor=CENTER)
table.heading("Publisher", text="Publisher", anchor=CENTER)
table.heading("Price", text="Price", anchor=CENTER)
table.heading("Page", text="Page", anchor=CENTER)
table.heading("Score", text="Score", anchor=CENTER)
table.pack()
table_frame.place(x=30,y=160)


searchButton =Button(mainPage, text='Search', width=15,fg=txtColor, bg=inside,
                     relief="ridge",highlightcolor=border,command=partial(get_condition)) #
searchButton.place(x=400,y=90)


getAllButton =Button(mainPage, text='Get All', width=15,fg=txtColor, bg=inside,
                     relief="ridge",highlightcolor=border,command=partial(get_All,table))
getAllButton.place(x=550,y=90)


addButton =Button(mainPage, text='Add Book', width=15,fg=txtColor, bg=inside,
                     relief="ridge",highlightcolor=border,command=add_book)
addButton.place(x=60,y=430)


updadeButton =Button(mainPage, text='Update Prices', width=15,fg=txtColor, bg=inside,
                     relief="ridge",highlightcolor=border,state=DISABLED,command=open_new_window)
updadeButton.place(x=260,y=430)


deleteButton =Button(mainPage, text='Delete Book', width=15,fg=txtColor, bg=inside,
                     relief="ridge",highlightcolor=border,state=DISABLED,command=delete_book)
deleteButton.place(x=460,y=430)



mainPage.geometry("700x500")
mainPage.title("Bookish Admin Page")
mainPage.configure(bg= bgColor)
mainPage.mainloop()
