from tkinter import *
import time

root = Tk()
root.geometry("1350x750+0+0")
root.title("Food Billing System")
root.configure(background='saddle brown')

Tops = Frame(root, bg='saddle brown', bd=20, pady=5, relief=RIDGE)
Tops.pack(side=TOP)

lblTitle=Label(Tops,font=('Times', 60, 'bold'), text='CAFE COFFEEDAY', bd=21, bg='black',
               fg='cornsilk', justify=CENTER)
lblTitle.grid(row=0)


ReceiptCal_F = Frame(root, bg='saddle brown', bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F = Frame(ReceiptCal_F, bg='saddle brown', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F = Frame(ReceiptCal_F, bg='saddle brown', bd=6, relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F = Frame(ReceiptCal_F, bg='saddle brown', bd=4, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root, bg='saddle brown', bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F = Frame(MenuFrame, bg='saddle brown', bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F = Frame(MenuFrame, bg='saddle brown', bd=4)
Drinks_F.pack(side=TOP)


Drinks_F = Frame(MenuFrame, bg='saddle brown', bd=4, relief=RIDGE)
Drinks_F.pack(side=LEFT)
Food_F = Frame(MenuFrame, bg='saddle brown', bd=4, relief=RIDGE)
Food_F.pack(side=RIGHT)

###################################################variables################################################

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofFood = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

E_Chocolate = StringVar()
E_Vanilla = StringVar()
E_Americano = StringVar()
E_Tea = StringVar()
E_Cappuccino = StringVar()
E_Espresso = StringVar()
E_Latte = StringVar()
E_ColdCoffee = StringVar()

E_HotDog = StringVar()
E_VegBurger = StringVar()
E_Pasta = StringVar()
E_HamBurger = StringVar()
E_Sandwich = StringVar()
E_Fries = StringVar()
E_Donuts = StringVar()
E_Pizza = StringVar()

E_Chocolate.set("0")
E_Vanilla.set("0")
E_Americano.set("0")
E_Tea.set("0")
E_Cappuccino.set("0")
E_Espresso.set("0")
E_Latte.set("0")
E_ColdCoffee.set("0")

E_HotDog.set("0")
E_VegBurger.set("0")
E_Pasta.set("0")
E_HamBurger.set("0")
E_Sandwich.set("0")
E_Fries.set("0")
E_Donuts.set("0")
E_Pizza.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))

root.mainloop()
