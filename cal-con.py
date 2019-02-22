from Tkinter import *
root=Tk()
root.title("CONVERTOR")
root.attributes("-fullscreen",True)
root.configure(background='cornsilk')

convert = DoubleVar()
currency = DoubleVar()

fr = Frame(root,height=80,width=2000,bg='gold')
fr.place(rely=.1)
labelfr=Label(fr,text='CONVERTOR',font='Arial 30 bold italic',bg='gold')
labelfr.place(relx=.3,rely=.2)
fr0 = Frame(root,height=80,width=2000,bg='gold')
fr0.place(rely=.8)
fr1 = Frame(root,height=1000,width=80,bg='gold',bd=10)
fr1.place(relx=.85)
fr2 = Frame(root,height=1000,width=80,bg='gold',bd=10)
fr2.place(relx=.1)
        
label=Label(root,text='Indian Rupee equals :',font="Arial 18 bold",bg='aliceblue',fg='royalblue')
label.place(relx=.25,rely=.301)
e=Entry(root,bd=4,width=15,font='Arial 15',textvariable=convert,justify='center')
e.place(relx=.5,rely=.307)

var = StringVar(root)
var.set("Curreny button")

def grab_and_assign(event):
    chosen_option = var.get()
    label_chosen_variable= Label(root, text=chosen_option)
    label_chosen_variable.grid(row=1, column=2)
        

drop_menu = OptionMenu(root, var,  "Brazil", "Canada", "Euro", "Kenya", "Nigeria", "Philippine", "USA", command=grab_and_assign)
drop_menu.place(relx=.5,rely=.406)
label1=Label(root,text='Currency 2 :',font="Arial 18 bold",textvariable=currency,bg='aliceblue',fg='royalblue')
label1.place(relx=.25,rely=.401)

def Reset():
    var.set("")
    convert.set("0.0")
    currency.set("0.0")

def ConCurrency():
    if var.get()=="USA":
        convert1 = float(convert.get() * 0.0153435)
        convert2 = "USA Dollars",str('%.2f' %(convert1))
        currency.set(convert2)

    elif var.get()=="Nigeria":
        convert1 = float(convert.get() * 5.45458)
        convert2 = "Nigerian Naira",str('%2f' %(convert1))
        currency.set(convert2)

    elif var.get()=="Brazil":
        convert1 = float(convert.get() * 0.0503039)
        convert2 = "Brazilian Real",str('%2f' %(convert1))
        currency.set(convert2)
            
    elif var.get()=="Canada":
        convert1 = float(convert.get() * 0.0194488)
        convert2 = "Canadian Dollar",str('%2f' %(convert1))
        currency.set(convert2)

    elif var.get()=="Euro":
        convert1 = float(convert.get() * 0.0131528)
        convert2 = "Euro",str('%2f' %(convert1))
        currency.set(convert2)
            
    elif var.get()=="Kenya":
        convert1 = float(convert.get() * 1.58810)
        convert2 = "Kenyian Shilling",str('%2f' %(convert1))
        currency.set(convert2)

    elif var.get()=="Philippine":
        convert1 = float(convert.get() * 0.786832)
        convert2 = "Philippine Peso",str('%2f' %(convert1))
        currency.set(convert2)



btnConvert = Button(root,text='Convert',font='Helvetica 9 bold',bg='salmon',bd=5,height=2,width=10,command=ConCurrency).place(relx=.25,rely=.67)
btnReset = Button(root,text='Reset',command=Reset,font='Helvetica 9 bold',bg='salmon',bd=5,height=2,width=10).place(relx=.4,rely=.67)
Button(root,text="Close",font='Helvetica 9 bold',bg='salmon',bd=5,height=2,width=10,command=lambda:root.destroy()).place(relx=.57,rely=.67)
def calculator():
    root=Tk()
    root.title("CALCULATOR")
    root.attributes("-fullscreen",True)
    root.configure(background='cornsilk')

    fr = Frame(root,height=80,width=2000,bg='gold')
    fr.place(rely=.1)
    labelfr=Label(fr,text='CALCULATOR',font='Arial 30 bold italic',bg='gold')
    labelfr.place(relx=.3,rely=.2)
    fr0 = Frame(root,height=80,width=2000,bg='gold')
    fr0.place(rely=.8)
    fr1 = Frame(root,height=1000,width=80,bg='gold',bd=10)
    fr1.place(relx=.85)
    fr2 = Frame(root,height=1000,width=80,bg='gold',bd=10)
    fr2.place(relx=.1)

    label=Label(root,text='First Number :',font="Arial 18 bold",bg='aliceblue',fg='royalblue')
    label.place(relx=.25,rely=.3)
    e=Entry(root,bd=2,width=15,font='Arial 15',justify='center')
    e.place(relx=.5,rely=.3)

    label1=Label(root,text='Second Number :',font="Arial 18 bold",bg='aliceblue',fg='royalblue')
    label1.place(relx=.25,rely=.4)
    e1=Entry(root,bd=2,width=15,font='Arial 15',justify='center')
    e1.place(relx=.5,rely=.4)

    def add():
        w=int(e.get())+int(e1.get())
        Label(root,text=w,font="Arial 18 bold",bg='aliceblue',fg='royalblue').place(relx=.25,rely=.5)
    def subtract():
        x=int(e.get())-int(e1.get())
        Label(root,text=x,font="Arial 18 bold",bg='aliceblue',fg='royalblue').place(relx=.4,rely=.5)
    def divide():
        y=int(e.get())/int(e1.get())
        Label(root,text=y,font="Arial 18 bold",bg='aliceblue',fg='royalblue').place(relx=.55,rely=.5)
    def multiply():
        z=int(e.get())*int(e1.get())
        Label(root,text=z,font="Arial 18 bold",bg='aliceblue',fg='royalblue').place(relx=.7,rely=.5)
        
    Button(root,text="ADD",command=add,font='Helvetica 8 bold',bg='salmon',bd=4,height=3,width=10).place(relx=.25,rely=.55)
    Button(root,text="SUBTRACT",command=subtract,font='Helvetica 8 bold',bg='salmon',bd=4,height=3,width=10).place(relx=.4,rely=.55)
    Button(root,text="DIVIDE",command=divide,font='Helvetica 8 bold',bg='salmon',bd=4,height=3,width=10).place(relx=.55,rely=.55)
    Button(root,text="MULTIPLY",command=multiply,font='Helvetica 8 bold',bg='salmon',bd=4,height=3,width=10).place(relx=.7,rely=.55)
    
    Button(root,text="Close",font='Helvetica 9 bold',bg='salmon',bd=7,height=2,width=10,command=lambda:root.destroy()).place(relx=.5,rely=.67)

Button(root,text="CALCULATOR",font='Helvetica 9 bold',bg='salmon',bd=5,height=2,width=10,command=calculator).place(relx=.7,rely=.67)

root.mainloop()




