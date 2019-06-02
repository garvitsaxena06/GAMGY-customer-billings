from tkinter import *
import time
import datetime
import random
import tkinter.messagebox

root =Tk()
root.geometry("1350x750+0+0")
root.title("Food Billing System")
root.configure(background='saddle brown')

Tops = Frame(root,bg='saddle brown',bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)

lblTitle=Label(Tops,font=('Times',60,'bold'),text='CAFE COFFEEDAY',bd=21,bg='black',
                fg='cornsilk',justify=CENTER)
lblTitle.grid(row=0)


ReceiptCal_F = Frame(root,bg='saddle brown',bd=10,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F,bg='saddle brown',bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_F,bg='saddle brown',bd=6,relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F=Frame(ReceiptCal_F,bg='saddle brown',bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root,bg='saddle brown',bd=10,relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame,bg='saddle brown',bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame,bg='saddle brown',bd=4)
Drinks_F.pack(side=TOP)


Drinks_F=Frame(MenuFrame,bg='saddle brown',bd=4,relief=RIDGE)
Drinks_F.pack(side=LEFT)
Food_F=Frame(MenuFrame,bg='saddle brown',bd=4,relief=RIDGE)
Food_F.pack(side=RIGHT)

###################################################variables################################################

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

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

##########################################Function Declaration####################################################

def iExit():
    iExit=tkinter.messagebox.askyesno("Exit Restaurant System","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofFood.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)


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

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)


    txtChocolate.configure(state=DISABLED)
    txtVanillaconfigure(state=DISABLED)
    txtAmericano.configure(state=DISABLED)
    txtTea.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtEspresso.configure(state=DISABLED)
    txtLatte.configure(state=DISABLED)
    txtColdCoffee.configure(state=DISABLED)
    txtHotDog.configure(state=DISABLED)
    txtVegBurger.configure(state=DISABLED)
    txtPasta.configure(state=DISABLED)
    txtHamBurger.configure(state=DISABLED)
    txtSandwich.configure(state=DISABLED)
    txtFries.configure(state=DISABLED)
    txtDonut.configure(state=DISABLED)
    txtPizza.configure(state=DISABLED)

def CostofItem():
    Item1=float(E_Chocolate.get())
    Item2=float(E_Vanilla.get())
    Item3=float(E_Americano.get())
    Item4=float(E_Tea.get())
    Item5=float(E_Cappuccino.get())
    Item6=float(E_Espresso.get())
    Item7=float(E_Latte.get())
    Item8=float(E_ColdCoffee.get())

    Item9=float(E_HotDog.get())
    Item10=float(E_VegBurger.get())
    Item11=float(E_Pasta.get())
    Item12=float(E_HamBurger.get())
    Item13=float(E_Sandwich.get())
    Item14=float(E_Fries.get())
    Item15=float(E_Donuts.get())
    Item16=float(E_Pizza.get())

    PriceofDrinks =(Item1 * 60) + (Item2 * 75) + (Item3 * 90) + (Item4 * 20) + (Item5 * 180) + (Item6 * 75) + (Item7 * 75) + (Item8 * 80)

    PriceofFood =(Item9 * 45) + (Item10 * 45) + (Item11 * 150) + (Item12 * 80) + (Item13 * 80) + (Item14 * 110) + (Item15 * 40) + (Item16 * 250)



    DrinksPrice = "Rs",str('%.2f'%(PriceofDrinks))
    FoodPrice =  "Rs",str('%.2f'%(PriceofFood))
    CostofFood.set(FoodPrice)
    CostofDrinks.set(DrinksPrice)
    SC = "Rs",str('%.2f'%(1.59))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rs",str('%.2f'%(PriceofDrinks + PriceofFood + 1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax = "Rs",str('%.2f'%((PriceofDrinks + PriceofFood + 1.59) * 0.15))
    PaidTax.set(Tax)

    TT=((PriceofDrinks + PriceofFood + 1.59) * 0.15)
    TC="Rs",str('%.2f'%(PriceofDrinks + PriceofFood + 1.59 + TT))
    TotalCost.set(TC)


def chkChocolate():
    if(var1.get() == 1):
        txtChocolate.configure(state = NORMAL)
        txtChocolate.focus()
        txtChocolate.delete('0',END)
        E_Chocolate.set("")
    elif(var1.get() == 0):
        txtChocolate.configure(state = DISABLED)
        E_Chocolate.set("0")

def chkVanilla():
    if(var2.get() == 1):
        txtVanilla.configure(state = NORMAL)
        txtVanilla.focus()
        txtVanilla.delete('0',END)
        E_Vanilla.set("")
    elif(var2.get() == 0):
        txtVanilla.configure(state = DISABLED)
        E_Vanilla.set("0")

def chkAmericano():
    if(var3.get() == 1):
        txtAmericano.configure(state = NORMAL)
        txtAmericano.delete('0',END)
        txtAmericano.focus()
    elif(var3.get() == 0):
        txtAmericano.configure(state = DISABLED)
        E_Americano.set("0")

def chkTea():
    if(var4.get() == 1):
        txtTea.configure(state = NORMAL)
        txtTea.delete('0',END)
        txtTea.focus()
    elif(var4.get() == 0):
        txtTea.configure(state = DISABLED)
        E_Tea.set("0")

def chkCappuccino():
    if(var5.get() == 1):
        txtCappuccino.configure(state = NORMAL)
        txtCappuccino.delete('0',END)
        txtCappuccino.focus()
    elif(var5.get() == 0):
        txtCappuccino.configure(state = DISABLED)
        E_Cappuccino.set("0")

def chkEspresso():
    if(var6.get() == 1):
        txtEspresso.configure(state = NORMAL)
        txtEspresso.delete('0',END)
        txtEspresso.focus()
    elif(var6.get() == 0):
        txtEspresso.configure(state = DISABLED)
        E_Espresso.set("0")

def chkLatte():
    if(var7.get() == 1):
        txtLatte.configure(state = NORMAL)
        txtLatte.delete('0',END)
        txtLatte.focus()
    elif(var7.get() == 0):
        txtLatte.configure(state = DISABLED)
        E_Latte.set("0")

def chkColdCoffee():
    if(var8.get() == 1):
        txtColdCoffee.configure(state = NORMAL)
        txtColdCoffee.delete('0',END)
        txtColdCoffee.focus()
    elif(var8.get() == 0):
        txtColdCoffee.configure(state = DISABLED)
        E_ColdCoffee.set("0")

def chkHotDog():
    if(var9.get() == 1):
        txtHotDog.configure(state = NORMAL)
        txtHotDog.delete('0',END)
        txtHotDog.focus()
    elif(var9.get() == 0):
        txtHotDog.configure(state = DISABLED)
        E_HotDog.set("0")

def chkVegBurger():
    if(var10.get() == 1):
        txtVegBurger.configure(state = NORMAL)
        txtVegBurger.delete('0',END)
        txtVegBurger.focus()
    elif(var10.get() == 0):
        txtVegBurger.configure(state = DISABLED)
        E_VegBurger.set("0")

def chkPasta():
    if(var11.get() == 1):
        txtPasta.configure(state = NORMAL)
        txtPasta.delete('0',END)
        txtPasta.focus()
    elif(var11.get() == 0):
        txtPasta.configure(state = DISABLED)
        E_Pasta.set("0")

def chkHamBurger():
    if(var12.get() == 1):
        txtHamBurger.configure(state = NORMAL)
        txtHamBurger.delete('0',END)
        txtHamBurger.focus()
    elif(var12.get() == 0):
        txtHamBurger.configure(state = DISABLED)
        E_HamBurger.set("0")

def chkSandwich():
    if(var13.get() == 1):
        txtSandwich.configure(state = NORMAL)
        txtSandwich.delete('0',END)
        txtSandwich.focus()
    elif(var13.get() == 0):
        txtSandwich.configure(state = DISABLED)
        E_Sandwich.set("0")

def chkFries():
    if(var14.get() == 1):
        txtFries.configure(state = NORMAL)
        txtFries.delete('0',END)
        txtFries.focus()
    elif(var14.get() == 0):
        txtFries.configure(state = DISABLED)
        E_Fries.set("0")

def chkDonut():
    if(var15.get() == 1):
        txtDonut.configure(state = NORMAL)
        txtDonut.delete('0',END)
        txtDonut.focus()
    elif(var15.get() == 0):
        txtDonut.configure(state = DISABLED)
        E_Donuts.set("0")

def chkPizza():
    if(var16.get() == 1):
        txtPizza.configure(state = NORMAL)
        txtPizza.delete('0',END)
        txtPizza.focus()
    elif(var16.get() == 0):
        txtPizza.configure(state = DISABLED)
        E_Pizza.set("0")

def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(1,500)
    randomRef= str(x)
    Receipt_Ref.set("Bill"+ randomRef)


    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() +'\t'+ DateofOrder.get() +'\n')
    txtReceipt.insert(END,'Items\t\t\t\t'+"Cost of Items \n")
    txtReceipt.insert(END,'Chocolate:\t\t\t\t\t' + E_Chocolate.get() +'\n')
    txtReceipt.insert(END,'Vanilla:\t\t\t\t\t'+ E_Vanilla.get()+'\n')
    txtReceipt.insert(END,'Americano:\t\t\t\t\t'+ E_Americano.get()+'\n')
    txtReceipt.insert(END,'Tea:\t\t\t\t\t'+ E_Tea.get()+'\n')
    txtReceipt.insert(END,'Cappuccino:\t\t\t\t\t'+ E_Cappuccino.get()+'\n')
    txtReceipt.insert(END,'Espresso:\t\t\t\t\t'+ E_Espresso.get()+'\n')
    txtReceipt.insert(END,'Latte:\t\t\t\t\t'+ E_Latte.get()+'\n')
    txtReceipt.insert(END,'ColdCoffee:\t\t\t\t\t'+ E_ColdCoffee.get()+'\n')
    txtReceipt.insert(END,'HotDog:\t\t\t\t\t'+ E_HotDog.get()+'\n')
    txtReceipt.insert(END,'VegBurger:\t\t\t\t\t'+ E_VegBurger.get()+'\n')
    txtReceipt.insert(END,'Pasta:\t\t\t\t\t'+ E_Pasta.get()+'\n')
    txtReceipt.insert(END,'HamBurger:\t\t\t\t\t'+ E_HamBurger.get()+'\n')
    txtReceipt.insert(END,'Sandwich:\t\t\t\t\t'+ E_Sandwich.get()+'\n')
    txtReceipt.insert(END,'Fries:\t\t\t\t\t'+ E_Fries.get()+'\n')
    txtReceipt.insert(END,'Donuts:\t\t\t\t\t'+ E_Donuts.get()+'\n')
    txtReceipt.insert(END,'Pizza:\t\t\t\t\t'+ E_Pizza.get()+'\n')
    txtReceipt.insert(END,'Cost of Drinks:\t\t\t\t\t'+ CostofDrinks.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
    txtReceipt.insert(END,'Cost of Foods:\t\t\t\t'+ CostofFood.get()+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
    txtReceipt.insert(END,'Service Charge:\t\t\t\t'+ ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")

root.mainloop()
