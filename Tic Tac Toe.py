from tkinter import *
from tkinter import messagebox

tk=Tk()
tk.title("My Project")
tk.configure(background='Grey')


a = StringVar()
i=1
c=True


def update(a):
    global i,c
    if i%2!=0 and c==True and a["text"]==" " :
        a["text"] = "X"
        w()
        i=i+1
        c=False
    elif i%2==0 and c==False and a["text"]==" " :
        a["text"] = "O"
        w()
        i = i + 1
        c = True
    elif a["text"]== "X":
        messagebox.showerror("Denied",p1.get()+" has already clicked this button")
    elif a["text"]== "O":
        messagebox.showerror("Denied",p2.get()+" has already clicked this button")


def e():

    for j in (button1,button2,button3,button4,button5,button9,button8,button7,button6,p2,p1):
        j.configure(state=DISABLED)




def w():
    if (button1['text']=='X' and button2['text']=='X' and button3['text']=='X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        messagebox.showinfo("WINNER", p1.get()+" Won this match \n WINNER WINNER CHICKEN DINNER")
        f = open("data.txt", "a")
        f.write("previous Winner:" + str(p1.get()) + "\n")
        f.close()
        e()

    elif(i == 9):
        messagebox.showinfo("Alas!", "It's a Tie,NO one Won")
        f = open("data.txt", "a")
        f.write("This match was a tie" + "\n")
        f.close()
        e()
    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
          messagebox.showinfo("WINNER", p2.get()+" Won this match \nWINNER WINNER CHICKEN DINNER")
          f = open("data.txt", "a")
          f.write("previous Winner:" + str(p2.get()) + "\n")
          f.close()
          e()




def re():
    global i,c
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "
    for j in (button1,button2,button3,button4,button5,button9,button8,button7,button6,p2,p1):
        j.configure(state=NORMAL)
    p1.delete(0, 'end')
    p2.delete(0, 'end')
    i = 1
    c = True

def l():
    messagebox.showerror("Access Denied","Login to know about last WINNER")
    j=Tk()
    j.title("Login")
    j.geometry('400x100')
    fa =Frame(j)
    fa.grid()
    j.wm_iconbitmap('l.ico')
    def de():
        if i1.get() == '@expert' and i2.get() == 'harjot':
            fa.grid_forget()
            f = open("data.txt", "r")
            j.destroy()
            messagebox.showinfo("Previous Winners", f.read())

            f.close()

        else:
            messagebox.showerror("Access Denied", "Wrong credentials")
            exit()

    l = Label(fa, text="Username: ",relief=RAISED, height=1, width=9, font='allstar 14 bold', bg='red', fg='white')
    l.grid(row=1, column=0)
    i1 = Entry(fa,bd=8,width=16,bg='blue',fg='white',font='anvil 14 bold')
    i1.grid(row=1, column=1)
    l = Label(fa, text="Password:",relief=RAISED, font='allstar 14 bold', bg='blue', fg='white', height=1, width=9)
    l.grid(row=2, column=0)
    i2 = Entry(fa,bd=8,width=16,bg='red',fg='white',font='anvil 14 bold')
    i2.grid(row=2, column=1)
    r = Button(fa, text="Login" ,font="algerian",bg='black',padx=5, fg='white', height=1, width=6, command=de)
    r.grid(row=4, column=1)


def v():
    exit()


p1 = Entry(tk,bd=14,width=23,bg='blue',fg='white',font='anvil 18 bold')
p1.grid(row=1,column=1,padx=0, columnspan=8)
p2 = Entry(tk,bd=14,width=23,bg='red',fg='white',font='anvil 18 bold')
p2.grid(row=2,column=1, columnspan=8)
label0 = Label( tk,relief=RAISED, text="Player 1:", font='allstar 18 bold', bg='red', fg='white', height=1, width=8)
label0.grid(row=1, column=0)
label1 = Label( tk,relief=RAISED, text="Player 2:", font='allstar 18 bold', bg='blue', fg='white', height=1, width=8)
label1.grid(row=2, column=0)
button1 = Button(tk, text=" ", font='Times 20 bold', bg='blue', fg='white', height=4, width=9, command=lambda:update(button1))
button1.grid(row=3, column=0)
button2 = Button(tk, text=' ', font='Times 20 bold', bg='red', fg='white', height=4, width=9, command=lambda: update(button2))
button2.grid(row=3, column=1)
button3 = Button(tk, text=' ',font='Times 20 bold', bg='blue', fg='white', height=4, width=8, command=lambda: update(button3))
button3.grid(row=3, column=2)
button4 = Button(tk, text=' ', font='Times 20 bold', bg='red', fg='white', height=4, width=9, command=lambda: update(button4))
button4.grid(row=4, column=0)
button5 = Button(tk, text=' ', font='Times 20 bold', bg='blue', fg='white', height=4, width=9, command=lambda: update(button5))
button5.grid(row=4, column=1)
button6 = Button(tk, text=' ', font='Times 20 bold', bg='red', fg='white', height=4, width=8, command=lambda: update(button6))
button6.grid(row=4, column=2)
button7 = Button(tk, text=' ', font='Times 20 bold', bg='blue', fg='white', height=4, width=9, command=lambda: update(button7))
button7.grid(row=5, column=0)
button8 = Button(tk, text=' ', font='Times 20 bold', bg='red', fg='white', height=4, width=9, command=lambda: update(button8))
button8.grid(row=5, column=1)
button9 = Button(tk, text=' ', font='Times 20 bold', bg='blue', fg='white', height=4, width=8, command=lambda: update(button9))
button9.grid(row=5, column=2)
button10=Button(tk,relief=RAISED, text="Restart",font="algerian",bg='black',padx=5, fg='white', height=1, width=13,command=re)
button10.grid(row=6, column=0)
buttonx=Button(tk,relief=RAISED, text="Previous Winners",font="algerian",bg='black',padx=5, fg='white', height=1, width=13,command=l)
buttonx.grid(row=6, column=1)
buttonx1=Button(tk,relief=RAISED, text="Exit",font="algerian",bg='black',padx=5, fg='white', height=1, width=12,command=v)
buttonx1.grid(row=6, column=2)
buttonx.config(highlightthickness=4)
button10.config(highlightthickness=3)
buttonx1.config(highlightthickness=3)


tk.mainloop()