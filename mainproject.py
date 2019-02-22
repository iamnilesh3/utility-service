import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox
import math 
from tkMessageBox import *
import os
import sqlite3

def intro():
    splash=Tk()
    splash.title('ABOUT THE DEVELOPER')
    splash.state('zoomed')
    icon1=PhotoImage(file="title.gif")
    l2=Label(splash,image=icon1)
    l2.pack()

    def dest():
        splash.destroy()
    splash.after(5000,dest)
    splash.mainloop()
intro()
root=Tk()
root.title("UTILITY")
root.attributes("-fullscreen",True)
root.configure(background='cornsilk')

def convertor():
    #root.destroy()
    root1=Toplevel()
    #root1=Tk()
    root1.title("CONVERTOR")
    root1.attributes("-fullscreen",True)
    root1.configure(background='cornsilk')

    convert = DoubleVar()
    currency = DoubleVar()

    fr = Frame(root1,height=80,width=2000,bg='Firebrick')
    fr.place(rely=.1)
    labelfr=Label(fr,text='CONVERTOR',font='Arial 30 bold underline italic',bg='gold')
    labelfr.place(relx=.3,rely=.2)
    fr0 = Frame(root1,height=80,width=2000,bg='Firebrick')
    fr0.place(rely=.8)
    fr1 = Frame(root1,height=1000,width=80,bg='Firebrick',bd=10)
    fr1.place(relx=.85)
    fr2 = Frame(root1,height=1000,width=80,bg='Firebrick',bd=10)
    fr2.place(relx=.1)
            
    label=Label(root1,text='Indian Rupee equals :',font="Arial 18 bold",bg='aliceblue',fg='royalblue')
    label.place(relx=.25,rely=.301)
    e=Entry(root1,bd=4,width=15,font='Arial 15',textvariable=convert,justify='center')
    e.place(relx=.5,rely=.307)

    var = StringVar(root1)
    var.set("Curreny button")

    def grab_and_assign(event):
        chosen_option = var.get()
        label_chosen_variable= Label(root1, text=chosen_option)
        label_chosen_variable.grid(row=1, column=2)
            

    drop_menu = OptionMenu(root1, var,  "Brazil", "Canada", "Euro", "Kenya", "Nigeria", "Philippine", "USA", command=grab_and_assign)
    drop_menu.place(relx=.5,rely=.406)
    label1=Label(root1,text='Currency 2 :',font="Arial 18 bold",textvariable=currency,bg='aliceblue',fg='royalblue')
    label1.place(relx=.25,rely=.401)

    def Reset():
        var.set("")
        convert.set("0.0")
        currency.set("0.0")

    def ConCurrency():
        if var.get()=="USA":
            convert1 = float(convert.get() * 0.0153435)
            convert2 = "USA Dollars ",str('%.2f' %(convert1))
            currency.set(convert2)

        elif var.get()=="Nigeria":
            convert1 = float(convert.get() * 5.45458)
            convert2 = "Nigerian Naira ",str('%2f' %(convert1))
            currency.set(convert2)

        elif var.get()=="Brazil":
            convert1 = float(convert.get() * 0.0503039)
            convert2 = "Brazilian Real ",str('%2f' %(convert1))
            currency.set(convert2)
                
        elif var.get()=="Canada":
            convert1 = float(convert.get() * 0.0194488)
            convert2 = "Canadian Dollar ",str('%2f' %(convert1))
            currency.set(convert2)

        elif var.get()=="Euro":
            convert1 = float(convert.get() * 0.0131528)
            convert2 = "Euro ",str('%2f' %(convert1))
            currency.set(convert2)
                
        elif var.get()=="Kenya":
            convert1 = float(convert.get() * 1.58810)
            convert2 = "Kenyian Shilling ",str('%2f' %(convert1))
            currency.set(convert2)

        elif var.get()=="Philippine":
            convert1 = float(convert.get() * 0.786832)
            convert2 = "Philippine Peso ",str('%2f' %(convert1))
            currency.set(convert2)



    btnConvert = Button(root1,text='Convert',font='Helvetica 9 bold',bg='salmon',bd=5,height=2,width=10,command=ConCurrency).place(relx=.25,rely=.67)
    btnReset = Button(root1,text='Reset',command=Reset,font='Helvetica 9 bold',bg='salmon',bd=5,height=2,width=10).place(relx=.4,rely=.67)
    Button(root1,text="Close",font='Helvetica 9 bold',bg='salmon',bd=5,height=2,width=10,command=lambda:root1.destroy()).place(relx=.57,rely=.67)

def calc():
    #root.destroy()
    root3=Toplevel()
    #root3=Tk()
    root3.title("CALCULATOR")
    root3.attributes("-fullscreen",True)
    root3.configure(background='cornsilk')

    fr = Frame(root3,height=80,width=2000,bg='Firebrick')
    fr.place(rely=.1)
    labelfr=Label(fr,text='CALCULATOR',font='Arial 30 bold underline italic',bg='gold')
    labelfr.place(relx=.3,rely=.2)
    fr0 = Frame(root3,height=80,width=2000,bg='Firebrick')
    fr0.place(rely=.8)
    fr1 = Frame(root3,height=1000,width=80,bg='Firebrick',bd=10)
    fr1.place(relx=.85)
    fr2 = Frame(root3,height=1000,width=80,bg='Firebrick',bd=10)
    fr2.place(relx=.1)

    label=Label(root3,text='First Number :',font="Arial 18 bold",bg='aliceblue',fg='royalblue')
    label.place(relx=.25,rely=.3)
    e=Entry(root3,bd=2,width=15,font='Arial 15',justify='center')
    e.place(relx=.5,rely=.3)

    label1=Label(root3,text='Second Number :',font="Arial 18 bold",bg='aliceblue',fg='royalblue')
    label1.place(relx=.25,rely=.4)
    e1=Entry(root3,bd=2,width=15,font='Arial 15',justify='center')
    e1.place(relx=.5,rely=.4)

    def add():
        w=int(e.get())+int(e1.get())
        Label(root3,text=w,font="Arial 18 bold",bg='aliceblue',fg='royalblue').place(relx=.25,rely=.5)
    def subtract():
        x=int(e.get())-int(e1.get())
        Label(root3,text=x,font="Arial 18 bold",bg='aliceblue',fg='royalblue').place(relx=.4,rely=.5)
    def divide():
        y=int(e.get())/int(e1.get())
        Label(root3,text=y,font="Arial 18 bold",bg='aliceblue',fg='royalblue').place(relx=.55,rely=.5)
    def multiply():
        z=int(e.get())*int(e1.get())
        Label(root3,text=z,font="Arial 18 bold",bg='aliceblue',fg='royalblue').place(relx=.7,rely=.5)
        
    Button(root3,text="ADD",command=add,font='Helvetica 8 bold',bg='salmon',bd=4,height=3,width=10).place(relx=.25,rely=.55)
    Button(root3,text="SUBTRACT",command=subtract,font='Helvetica 8 bold',bg='salmon',bd=4,height=3,width=10).place(relx=.4,rely=.55)
    Button(root3,text="DIVIDE",command=divide,font='Helvetica 8 bold',bg='salmon',bd=4,height=3,width=10).place(relx=.55,rely=.55)
    Button(root3,text="MULTIPLY",command=multiply,font='Helvetica 8 bold',bg='salmon',bd=4,height=3,width=10).place(relx=.7,rely=.55)
    
    Button(root3,text="Close",font='Helvetica 9 bold',bg='salmon',bd=7,height=2,width=10,command=lambda:root3.destroy()).place(relx=.5,rely=.67)

def lent():
    #root.destroy()
    root2=Toplevel()
    #root2=Tk()
    root2.title("Length Convertor")
    root2.attributes("-fullscreen",True)
    root2.configure(background='cornsilk')

    convert = DoubleVar()
    currency = DoubleVar()

    fr = Frame(root2,height=80,width=2000,bg='gold')
    fr.place(rely=.1)
    labelfr=Label(fr,text='Length Convertor',font='Arial 30 bold underline italic',bg='gold')
    labelfr.place(relx=.25,rely=.2)
    fr0 = Frame(root2,height=80,width=2000,bg='gold')
    fr0.place(rely=.8)
    fr1 = Frame(root2,height=1000,width=80,bg='gold',bd=10)
    fr1.place(relx=.85)
    fr2 = Frame(root2,height=1000,width=80,bg='gold',bd=10)
    fr2.place(relx=.1)

    label=Label(root2,text='This much Meters equals :',font="Arial 18 bold",bg='aliceblue',fg='royalblue')
    label.place(relx=.25,rely=.301)
    e=Entry(root2,bd=4,width=15,font='Arial 15',textvariable=convert,justify='center')
    e.place(relx=.5,rely=.307)

    var = StringVar(root2)
    var.set("Length button")

        
    def grab_and_assign(event):
        chosen_option = var.get()
        label_chosen_variable= Label(root2, text=chosen_option)
        label_chosen_variable.grid(row=1, column=2)
                

    drop_menu = OptionMenu(root2, var,  "CentiMeter", "KiloMeter", "MiliMeter", "MacroMeter", "NanoMeter", "Yard", "Foot", "Inch", command=grab_and_assign)
    drop_menu.place(relx=.53,rely=.406)
    label1=Label(root2,text='Length 2 :',font="Arial 18 bold",textvariable=currency,bg='aliceblue',fg='royalblue')
    label1.place(relx=.25,rely=.401)


    def Reset():
        var.set("")
        convert.set("0.0")
        currency.set("0.0")

    def ConLength():
        if var.get()=="CentiMeter":
            convert1 = float(convert.get() * 100)
            convert2 = "CentiMeter",str('%.2f' %(convert1))
            currency.set(convert2)

        elif var.get()=="KiloMeter":
            convert1 = float(convert.get() * 0.001)
            convert2 = "KiloMeter",str('%2f' %(convert1))
            currency.set(convert2)

        elif var.get()=="MiliMeter":
            convert1 = float(convert.get() * 1000)
            convert2 = "MiliMeter",str('%2f' %(convert1))
            currency.set(convert2)

        elif var.get()=="MacroMeter":
            convert1 = float(convert.get() * 100000)
            convert2 = "MacroMeter",str('%2f' %(convert1))
            currency.set(convert2)

        elif var.get()=="NanoMeter":
            convert1 = float(convert.get() * 100000000)
            convert2 = "NanoMeter",str('%2f' %(convert1))
            currency.set(convert2)

        elif var.get()=="Yard":
            convert1 = float(convert.get() * 1.09361)
            convert2 = "Yard",str('%2f' %(convert1))
            currency.set(convert2)

        elif var.get()=="Foot":
            convert1 = float(convert.get() * 3.28083)
            convert2 = "Foot",str('%2f' %(convert1))
            currency.set(convert2)
                    
        elif var.get()=="Inch":
            convert1 = float(convert.get() * 39.36996)
            convert2 = "Inch",str('%2f' %(convert1))
            currency.set(convert2)
           
    btnConvert = Button(root2,text='Convert',font='Helvetica 9 bold',bg='salmon',bd=5,height=2,width=10,command=ConLength).place(relx=.25,rely=.67)
    btnReset = Button(root2,text='Reset',command=Reset,font='Helvetica 9 bold',bg='salmon',bd=5,height=2,width=10).place(relx=.4,rely=.67)
    Button(root2,text="Close",font='Helvetica 9 bold',bg='salmon',bd=7,height=2,width=10,command=lambda:root2.destroy()).place(relx=.5,rely=.67)

def note():
    #root.destroy()
    root4=Toplevel()
    root4.title("TextEditor")
    root4.attributes("-fullscreen",True)
    textPad = ScrolledText(root4, width=100, height=80)

    def open_command():
            file = tkFileDialog.askopenfile(parent=root4,mode='rb',title='Select a file')
            if file != None:
                contents = file.read()
                textPad.insert('1.0',contents)
                file.close()

    def save_command(self):
        file = tkFileDialog.asksaveasfile(mode='w')
        if file != None:
            data = self.textPad.get('1.0', 'end-1c')
            file.write(data)
            file.close()
            
    def exit_command():
        if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
            root4.destroy()

    def about_command():
        label = tkMessageBox.showinfo("About", " TextEditor \n Copyright \n Rights reserved to Nilesh Singh ")
            

    def dummy():
        print ("I am a Dummy Command, I will be removed in the next step")

    menu = Menu(root4)
    root4.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New", command=dummy)
    filemenu.add_command(label="Open File", command=open_command)
    filemenu.add_command(label="Save", command=save_command)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exit_command)
    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=about_command)

    textPad.pack()
    root4.mainloop()



Button(root,text="Calculator",command=calc,font='Helvetica 12 bold',bg='Deep Sky Blue',bd=10,height=5,width=15).place(relx=.2,rely=.3)
Button(root,text="Convertor",command=convertor,font='Helvetica 12 bold',bg='Deep Sky Blue',bd=10,height=5,width=15).place(relx=.67,rely=.3)
Button(root,text="Length Conv",command=lent,font='Helvetica 12 bold',bg='Deep Sky Blue',bd=10,height=5,width=15).place(relx=.2,rely=.55)
Button(root,text="Notes",command=note,font='Helvetica 12 bold',bg='Deep Sky Blue',bd=10,height=5,width=15).place(relx=.67,rely=.55)

Button(root,text="Close",font='Helvetica 12 bold',bg='Deep Sky Blue',bd=7,height=2,width=12,command=lambda:root.destroy()).place(relx=.45,rely=.48)

fr = Frame(root,height=80,width=2000,bg='Firebrick')
fr.place(rely=.1)
labelfr=Label(fr,text='UTILITY',font='Arial 30 bold underline ',bg='gold')
labelfr.place(relx=.3,rely=.2)
fr0 = Frame(root,height=80,width=2000,bg='Firebrick')
fr0.place(rely=.8)
labelfr1=Label(fr0,text='By- Nilesh Singh',font='Arial 30 bold italic',bg='gold')
labelfr1.place(relx=.28,rely=.2)
fr1 = Frame(root,height=1000,width=80,bg='Firebrick',bd=10)
fr1.place(relx=.85)
fr2 = Frame(root,height=1000,width=80,bg='Firebrick',bd=10)
fr2.place(relx=.1)

root.mainloop()
