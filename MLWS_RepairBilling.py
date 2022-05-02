import os
import tempfile
from tkinter import ttk
from tkinter.ttk import Combobox, Style
from tkinter import *



# from turtle import clear, width

root=Tk()
root.title('Repair Billing Manangement System (Mahalaxmi Watch)')
root.geometry('1280x720')
# bg_color='#2D9290'
bg_color='#000000'

p1 = PhotoImage(file = '')


#=====================variables===================
varTitle=StringVar()
varName=StringVar()
varPhone_Number=StringVar()
varAddress=StringVar()
varBrand=StringVar()
varModel=StringVar()
varType=StringVar()
varDial_Style=StringVar()
varDial_Color=StringVar()
varCase=StringVar()
varStrap=StringVar()
varRemarks=StringVar()
varTotalCost=StringVar()
varAdvanceCost=StringVar()
varDueCost=StringVar()
varDay=StringVar()
varMonth=StringVar()
varYear=StringVar()

# def exit():
#     if messagebox.askyesno('Exit','Do you really want to exit'):
#         root.destroy()

def submit():
    import mysql.connector
    myDb = mysql.connector.connect(user='root', password='MLWS2022', host='localhost', database='sys')
    myCursor = myDb.cursor()
    
    sql_string_cust_dtls = f'''insert into sys.cust_dtls values({varPhone_Number.get()},"{varTitle.get()}","{varName.get()}","{varAddress.get()}");'''
    myCursor.execute(sql_string_cust_dtls)

    sql_string_prdct_dtls = f'''insert into sys.prdct_dtls values("{varBrand.get()}","{varModel.get()}","{varType.get()}","{varDial_Style.get()}","{varDial_Color.get()}","{varCase.get()}","{varStrap.get()}","{varRemarks.get()}","{varPhone_Number.get()}");'''
    myCursor.execute(sql_string_prdct_dtls)
    
    myDb.commit()
    myDb.close()

def print_fn():
    q=textarea.get('1.0','end-1c')
    filename=tempfile.mktemp('.txt')
    open(filename,'w').write(q)
    os.startfile(filename,'Print')

def receipt():
    textarea.delete(1.0,END)
    textarea.insert(END,'-------------------------------------------------------\n')
    textarea.insert(END,' Customer Details\n')
    textarea.insert(END,'-------------------------------------------------------')
    textarea.insert(END,f'\nName: \t{varTitle.get()} {varName.get().capitalize()}')
    textarea.insert(END,f'\nPhone Number: \t+91 {varPhone_Number.get()}')
    textarea.insert(END,f'\nAddress: \t{varAddress.get().capitalize()}')
    textarea.insert(END,'\n-------------------------------------------------------')
    textarea.insert(END,'\n-------------------------------------------------------')

    textarea.insert(END,'\n Product Details')
    textarea.insert(END,'\n-------------------------------------------------------')
    textarea.insert(END,f'\n Brand Name: \t{varBrand.get()}')
    textarea.insert(END,f'\n Model Number: \t{varModel.get()}')
    textarea.insert(END,f'\n Type: \t\t{varType.get()}')
    textarea.insert(END,f'\n Dial Shape: \t{varDial_Style.get()}')
    textarea.insert(END,f'\n Dial Color: \t{varDial_Color.get()}')
    textarea.insert(END,f'\n Case Shape: \t{varCase.get()}')
    textarea.insert(END,f'\n Strap: \t{varStrap.get()}')
    textarea.insert(END,f'\n Remarks: \t{varRemarks.get()}')
    textarea.insert(END,'\n-------------------------------------------------------')
    textarea.insert(END,'\n-------------------------------------------------------')

    textarea.insert(END,'\n Delivery Details')
    textarea.insert(END,'\n-------------------------------------------------------')
    textarea.insert(END,f'\n Total Amount To Be Paid: \t{varTotalCost.get()}')
    textarea.insert(END,f'\n Amount Paid in Advance: \t{varAdvanceCost.get()}')
    textarea.insert(END,f'\n Amount Due: \t\t{int(varTotalCost.get())-int(varAdvanceCost.get())}')
    textarea.insert(END,f'\n Expected Delivery Date: \t{varDay.get()}-{varMonth.get()}-{varYear.get()}')


title=Label(root,pady=5,text="Billing Manangement System",bd=12,bg=bg_color,fg='white',font=('times new roman', 35 ,'bold'),relief='flat',justify=CENTER)
title.pack(fill=X)

#===============Product Details=================
F1 = LabelFrame(root, text='Customer Details', font=('times new romon', 18, 'bold'), fg='gold',bg=bg_color,bd=15,relief='flat')
F1.place(x=5, y=90,width=800,height=180)

varTitle_lbl=Label(F1, text='Title: ', font=("Helvetica",13), fg='lawngreen',bg=bg_color)
varTitle_lbl.place(x=20, y=10)
title_Variable_Set = ("Mr.","Ms.","Mrs.","N/A")
varTitle = Combobox(F1, state="readonly", values=title_Variable_Set,textvariable=varTitle, width=4)
varTitle.place(x=60, y=10)

varName_lbl=Label(F1, text='Name: ', font=("Helvetica",13), fg='lawngreen',bg=bg_color)
varName_lbl.place(x=150, y=10)
varName = Entry(F1, textvariable=varName, width=31)
varName.place(x=205, y=10)

varPhone_Number_lbl = Label(F1, text='Phone Number: ', font=("Helvetica", 13), fg='lawngreen', bg=bg_color)
varPhone_Number_lbl.place(x=20, y=50)
varPhone_Number = Entry(F1, textvariable=varPhone_Number, width=14)
varPhone_Number.place(x=142, y=50)

varAddress_lbl = Label(F1, text='Address: ', font=("Helvetica", 13), fg='lawngreen', bg=bg_color)
varAddress_lbl.place(x=20, y=90)
varAddress = Entry(F1, textvariable=varAddress, width=50)
varAddress.place(x=93, y=90)

#Product Details
F2 = LabelFrame(root, text='Product Details', font=('times new romon', 18, 'bold'), fg='gold',bg=bg_color,bd=15,relief='flat')
F2.place(x=5, y=275, width=800,height=320)

varBrand_lbl = Label(F2, text='Brand: ', font=('Helvetica', 13), fg='lawngreen', bg=bg_color)
varBrand_lbl.place(x=20, y=10)
Brand_Variable_Set = ("Casio", "Fastrack", "Titan", "Sonata", "Timex", "Helix Timex", "AmazFit", "FireBoult", "RealMe", "Ajanta", "Ethnic", "Titan Clocks")
varBrand = Combobox(F2, values=Brand_Variable_Set)
varBrand.place(x=75, y=10)

varModel_lbl = Label(F2, text='Model Number: ', font=('Helvetica', 13), fg='lawngreen', bg=bg_color)
varModel_lbl.place(x=280, y=10)
varModel = Entry(F2, textvariable=varModel, width=18)
varModel.place(x=395, y=10)

varType_lbl = Label(F2, text='Type: ', font=('Helvetica', 13), fg='lawngreen', bg=bg_color)
varType_lbl.place(x=20, y=50)
varType1 = Radiobutton(F2, text="Gents", variable=varType, value='Gents', font=('Helvetica', 13), fg='chocolate', bg=bg_color)
varType1.place(x=100, y=50)
varType2 = Radiobutton(F2, text="Ladies", variable=varType, value='Ladies', font=('Helvetica', 13), fg='chocolate', bg=bg_color)
varType2.place(x=200, y=50)

varDial_Style_lbl = Label(F2, text='Dial Style: ', font=('Helvetica', 13), fg='lawngreen', bg=bg_color)
varDial_Style_lbl.place(x=20, y=90)
Dial_Shape_Set = ("Wide Dial", "Square Dial", "Oval Dial", "Quartz Dial")
varDial_Style = Combobox(F2, values=Dial_Shape_Set, state='readonly')
varDial_Style.place(x=100, y=90)

varDial_Color_lbl=Label(F2, text="Dial Color: ", font=('Helvetica', 13), fg='lawngreen', bg=bg_color)
varDial_Color_lbl.place(x=280, y=90)
Dial_Color_Set = ("Golden", "Silver", "White", "Black", "Red", "Blue", "Violet", "Green", "Yellow")
varDial_Color = Combobox(F2, values=Dial_Color_Set, state='readonly')
varDial_Color.place(x=365, y=90)

varCase_lbl=Label(F2, text="Case Shape: ", font=('Helvetica', 13), fg='lawngreen', bg=bg_color)
varCase_lbl.place(x=20, y=130)
Case_Shape_Set = ("Round", "Rectangular", "Square", "Cushion", "Barrel", "Assymmetrical", "Avant Grade")
varCase=Combobox(F2, values=Case_Shape_Set, state='readonly')
varCase.place(x=120, y=130)

varStrap_lbl=Label(F2, text="Strap: ", font=('Helvetica', 13), fg='lawngreen', bg=bg_color)
varStrap_lbl.place(x=280, y=130)
Strap_Set = ("Metal Bracelets", "Leather Watch", "Rubber Watch", "Silicone Watch", "Nylon Watch", "Canvas")
varStrap=Combobox(F2, values=Strap_Set, state='readonly')
varStrap.place(x=330,y=130)

varRemarks_lbl = Label(F2, text='Remarks: ', font=('Helvetica', 13), fg='lawngreen', bg=bg_color)
varRemarks_lbl.place(x=20, y=170)
varRemarks = Entry(F2, text="Remarks", state='normal', justify='center')
varRemarks.place(x=100, y=170, width=405)

varTotalCost_lbl = Label(F2, text='Total Cost: ', font=('Helvetica', 13), fg='lawngreen', bg=bg_color)
varTotalCost_lbl.place(x=20, y=210)
varTotalCost = Entry(F2, textvariable=varTotalCost, state='normal', justify='right')
varTotalCost.place(x=105, y=210, width=50)

varAdvanceCost_lbl = Label(F2, text='Advance Paid: ', font=('Helvetica', 13), fg='lawngreen', bg=bg_color)
varAdvanceCost_lbl.place(x=180, y=210)
varAdvanceCost = Entry(F2, textvariable=varAdvanceCost, state='normal', justify='right')
varAdvanceCost.place(x=295, y=210, width=50)

varDate_lbl = Label(F2, text='Expected Delivery Date: ', font=('Helvetica', 13), fg='lawngreen', bg=bg_color)
varDate_lbl.place(x=20, y=250)

Years = []
Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
Days=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)

for i in range(2021,2050):
    Years.append(i)

varYear = Combobox(F2, values=Years, state='readonly')
varYear.place(x=200, y=250, width=50)

varMonth = Combobox(F2, values=Months, state='readonly')
varMonth.place(x=250, y=250, width=85)

varDay = Combobox(F2, values=Days, state='readonly')
varDay.place(x=335,y=250,width=50)



#=====================Bill area====================
F3=Frame(root,relief='flat',bd=10)
F3.place(x=820,y=90,width=430,height=500)
bill_title=Label(F3,text='Receipt',font='arial 15 bold',bd=7,relief='flat').pack(fill=X)
scrol_y=Scrollbar(F3,orient=VERTICAL)
scrol_y.pack(side=RIGHT,fill=Y)
textarea=Text(F3,font='arial 15',yscrollcommand=scrol_y.set)
textarea.pack(fill=BOTH)
scrol_y.config(command=textarea.yview)

#=====================Buttons========================
F4 =Frame(root,bg='gray',bd=15,relief='ridge')
F4.place(x=5, y=590,width=1270,height=120)

btn2 = Button(F4, text='Receipt', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=receipt)
btn2.grid(row=0,column=1,padx=10,pady=10)

btn3 = Button(F4, text='Print', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=print_fn)
btn3.grid(row=0,column=2,padx=10,pady=10)

btn4 = Button(F4, text='Submit', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=submit)
btn4.grid(row=0,column=3,padx=10,pady=10)

# btn5 = Button(F4, text='Exit', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=exit)
# btn5.grid(row=0,column=4,padx=10,pady=10)

root.mainloop()