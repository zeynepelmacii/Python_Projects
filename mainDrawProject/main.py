from tkinter import *
from tkinter import messagebox
import database
import random


#functions
def display_list():
    part_list.delete(0,END)
    for row in database.select():
        part_list.insert(END,row)

def add_item():
    #eksik kontroller: age,phone string giremez messagebox göstermesi yapılmadı!!
    if name.get()=='' or lname.get()=='' or age.get()=='' or phone.get()=='':
        messagebox.showerror("ERROR !!", "please enter all informations")
        return
    if any(chr.isdigit() for chr in name.get()) or any(chr.isdigit() for chr in lname.get()):
        messagebox.showerror("ERROR !!", "please enter valid informations")
        return
    if age.get()<18:
        messagebox.showerror("ERROR !! ", "under 18 can not join")
        return

    database.insert(name.get(),lname.get(),age.get(),phone.get())
    part_list.delete(0,END)
    part_list.insert(0,(name.get(),lname.get(),age.get(),phone.get()))
    clear_input()
    display_list()

def select_item(event):
    try:
        global select_item
        index = part_list.curselection()[0]
        select_item = part_list.get(index)

        entName.delete(0,END)
        entName.insert(END, select_item[1])
        entLname.delete(0, END)
        entLname.insert(END, select_item[2])
        entAge.delete(0, END)
        entAge.insert(END, select_item[3])
        entPhone.delete(0, END)
        entPhone.insert(END, select_item[4])

        add_btn.configure(state=DISABLED)
        remove_btn.configure(state=NORMAL)
        update_btn.configure(state=NORMAL)
        clear_btn.configure(state=NORMAL)
    except IndexError:
        pass


def remove_item():
    messagebox.showinfo(">> REMOVING <<", "If you are sure, press the button.")
    database.delete(select_item[0])
    display_list()
    clear_input()

def update_item():
    database.update(name.get(),lname.get(),age.get(),phone.get(),select_item[0])
    display_list()

def clear_input():
    entName.delete(0, END)
    entLname.delete(0, END)
    entAge.delete(0, END)
    entPhone.delete(0, END)

def results():
    lblExpWinner = Label(rootFrame, text="Winner : ",font=('bold', 10), pady=20, fg=lblExpColor, bg=rootFrameColor)
    lblExpWinner.grid(row=10,column=2)

    lblExpSpare = Label(rootFrame, text="Spare : ", font=('bold', 10), pady=20, fg=lblExpColor, bg=rootFrameColor)
    lblExpSpare.grid(row=11, column=2)

    # set text winner and spare
    winner = chose_winner_or_spare()
    lblWinner = Label(rootFrame,text=winner, font=('bold', 10), pady=20, fg=lblExpColor, bg=rootFrameColor)
    lblWinner.grid(row=10,column=3)

    spare = chose_winner_or_spare()
    lblSpare = Label(rootFrame ,text=spare, font=('bold', 10), pady=20, fg=lblExpColor, bg=rootFrameColor)
    lblSpare.grid(row=11,column=3)

def chose_winner_or_spare():
    rndNumber=random.randint(0,part_list.size()-1)
    print(part_list.get(rndNumber))
    chose_btn.configure(state=DISABLED)
    return part_list.get(rndNumber)


def search_item():
    part_list.delete(0, END)
    for row in database.select_condition(nameForSearch.get()):
        part_list.insert(END,row)



#colors
rootFrameColor = '#FDFBF3'
lblExpColor = 'black'
btnBgColor = '#D3EEE1'
entry_highlight = '#D3EEE1'
listBox_highlight = '#D3EEE1'
button_highlight = '#D3EEE1'
part_listBg = "#D3EEE1"


#create myframe
rootFrame = Tk()



nameForSearch = StringVar()
entSearch = Entry(rootFrame, textvariable=nameForSearch)
entSearch.grid(row=16, column=0)
entSearch.configure(highlightthickness=1,highlightbackground=entry_highlight)

search_btn =Button(rootFrame, text='Search Participant', width=15, command=search_item,
                 fg='black', bg=btnBgColor, relief="ridge")
search_btn.grid(row=16,column=1,pady=20,padx=10)
search_btn.configure(borderwidth=3)


#name part
name = StringVar()
lblNameExp = Label(rootFrame, text='Name : ', font=('bold', 10), pady=20, fg=lblExpColor, bg=rootFrameColor)
lblNameExp.grid(row=0, column=0, sticky=W)
entName = Entry(rootFrame, textvariable=name)
entName.grid(row=0, column=1)
entName.configure(highlightthickness=1,highlightbackground=entry_highlight)

#lname part
lname = StringVar()
lblLnameExp = Label(rootFrame, text='Surname : ', font=('bold', 10), fg=lblExpColor, bg=rootFrameColor,)
lblLnameExp.grid(row=1, column=0, sticky=W)
entLname = Entry(rootFrame, textvariable=lname)
entLname.grid(row=1, column=1)
entLname.configure(highlightthickness=1,highlightbackground=entry_highlight)

# age part
age = IntVar()
lblAgeExp = Label(rootFrame, text='Age : ', font=('bold', 10), fg=lblExpColor, bg=rootFrameColor)
lblAgeExp.grid(row=0, column=2, sticky=W)
entAge = Entry(rootFrame, textvariable=age)
entAge.grid(row=0, column=3)
entAge.configure(highlightthickness=1,highlightbackground=entry_highlight)

#phone num part
phone = StringVar()
lblPhoneExp = Label(rootFrame, text='Phone : ', font=('bold', 10), fg=lblExpColor, bg=rootFrameColor)
lblPhoneExp.grid(row=1, column=2, sticky=W)
entPhone = Entry(rootFrame, textvariable=phone)
entPhone.grid(row=1, column=3)
entPhone.configure(highlightthickness=1,highlightbackground=entry_highlight)


#participant list
part_list = Listbox(rootFrame, height=12, width=70, border=0)
part_list.grid(row=4,column=0,columnspan=4,rowspan=6,pady=5,padx=20)
part_list.configure(background=part_listBg,foreground="black",highlightbackground=listBox_highlight,highlightthickness=2)
part_list.bind('<<ListboxSelect>>',  select_item) #bind item selection



#buttons
add_btn =Button(rootFrame, text='Add Participant', width=15, command=add_item,
                 fg='black', bg=btnBgColor, relief="ridge")
add_btn.grid(row=3,column=0,pady=20,padx=10)
add_btn.configure(borderwidth=3)

remove_btn =Button(rootFrame, text='Remove Participant', width=15, command=remove_item,
                   fg='black', bg=btnBgColor, relief="ridge", state= DISABLED)
remove_btn.grid(row=3,column=1,padx=10)
remove_btn.configure(borderwidth=3)

update_btn =Button(rootFrame, text='Update Participant', width=16, command=update_item,
                   fg='black', bg=btnBgColor, relief="ridge", state= DISABLED)
update_btn.grid(row=3,column=2,padx=10)
update_btn.configure(borderwidth=3)

clear_btn =Button(rootFrame, text='Clear Input', width=16, command=clear_input,
                  fg='black', bg=btnBgColor, relief="ridge", state= DISABLED)
clear_btn.grid(row=3,column=3,padx=10)
clear_btn.configure(borderwidth=3)

chose_btn =Button(rootFrame, text='Chose a lucky one !', height=1, width=24, command=results,
                  fg='black', bg=btnBgColor, relief="ridge")
chose_btn.grid(row=10,column=1)
chose_btn.configure(borderwidth=3)




rootFrame.geometry('700x500')
rootFrame.title('Draw Register')
rootFrame.configure(bg=rootFrameColor)

#display data
display_list()

rootFrame.mainloop()