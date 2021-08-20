from tkinter import *
from tkinter import ttk
import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='databasename')
mycursor = mydb.cursor()

# ------------------ All Functions ------------------

def go_to_add():
    mainpage.pack_forget()
    frame1.pack()

def go_to_view():
    mainpage.pack_forget()
    frame2.pack()
    display2()

def go_to_upd():
    mainpage.pack_forget()
    frame3.pack()
    clr4()
    display3()

def go_to_del():
    mainpage.pack_forget()
    frame4.pack()
    display4()

def menu1():
    frame1.pack_forget()
    mainpage.pack()

def menu2():
    frame2.pack_forget()
    mainpage.pack()

def menu3():
    frame3.pack_forget()
    mainpage.pack()

def menu4():
    frame4.pack_forget()
    mainpage.pack()

def clear_added_text():
    # delete from start to stop
    item_name.delete('0','end')
    price.delete('0','end')
    date.delete('0','end')
    category.delete('0','end')
    # cursor focus
    item_name.focus_set()
# ----------------------- Main GUI Window -----------------------

root = Tk()
root.title('Expenditure Log')
root.minsize(400,400)
style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 10)) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 11,'bold')) # Modify the font of the headings
style.configure('Treeview', rowheight=50)

# First the image shd be the object of PhotoImage()..
icon = PhotoImage(file='as.png')
# For titlebar icon
root.iconphoto(False,icon)

list_dict = {'name':[],'price':[],'category':[],'date':[]}

# -------------------- MainPage (Start Page)-------------------------

mainpage = Frame(root, width=290, height=290)
# mainpage['bg'] ='#fb0'
lab_mp= Label(mainpage,text='Welcome To PyGUI Expenditure Log !!',font=("Arial",13,'bold'))
lab_mp.pack(pady=15)
add_exp_btn = Button(mainpage,text='Add Entry',bg='yellow',font=("Algerian",13),command=go_to_add)
add_exp_btn.pack(pady=15)
view_exp_btn = Button(mainpage,text='View All Entries',bg='skyblue',font=("Algerian",13),command=go_to_view)
view_exp_btn.pack(pady=15)
update_exp_btn = Button(mainpage,text='Update Entry',bg='lightgreen',font=("Algerian",13),command=go_to_upd)
update_exp_btn.pack(pady=15)
del_exp_btn = Button(mainpage,text='Delete Entry',bg='orange',font=("Algerian",13),command=go_to_del)
del_exp_btn.pack(pady=15)
exit_btn = Button(mainpage,text='EXIT',bg='red',font=("Algerian",13),command=root.destroy)
exit_btn.pack(pady=15)

# -------------------- FRAME 1 Add Entry ------------------------

def add_entry():
    # PLace the data to save data.
    list_dict['name'].append(item_name.get())
    list_dict['price'].append(price.get())
    list_dict['category'].append(category.get())
    list_dict['date'].append(date.get())

#     storing data to mysql database
    sql ='insert into expenditure (Item_Name,Price,Category,Date) values (%s, %s, %s, %s) '
    vals = (item_name.get(),price.get(),category.get(),date.get())
    mycursor.execute(sql,vals)
    mydb.commit()

    clear_added_text()


frame1 = Frame(root, width=350, height=350)

top_lab = Label(frame1,text='Enter The Details Below !!',font=("Arial",14,'bold'))
top_lab.place(x=60,y=10)

lab_name = Label(frame1,text='Item Name :',font=("Arial",12))
lab_name.place(x=40,y=55)
item_name = Entry(frame1)
item_name.place(x=150,y=60 )

lab_price = Label(frame1,text='Price :',font=("Arial",12))
lab_price.place(x=40,y=95)
price = Entry(frame1)
price.place(x=150,y=100)

lab_date = Label(frame1,text='Date :',font=("Arial",12))
lab_date.place(x=40,y=135)
date = Entry(frame1)
date.place(x=150,y=140)

lab_cat = Label(frame1,text='Category :',font=("Arial",12))
lab_cat.place(x=40,y=175)
category = Entry(frame1)
category.place(x=150,y=180)

add_entry = Button(frame1,text='Add Entry',bg='lightblue',font=("Algerian",13),command=add_entry)
add_entry.place(x=120,y=235)

menu_f1 = Button(frame1,text='Back to Menu',bg='yellow',font=("Algerian",13),command=menu1)
menu_f1.place(x=105,y=305)

# -------------------- FRAME 2 View All Entries ------------------------
def display2():
    tv2.delete(*tv2.get_children())
    sql_select = "select * from expenditure"
    mycursor.execute(sql_select)
    records = mycursor.fetchall()
    # record_count = mycursor.rowcount
    for i in records:
        tv2.insert('','end',values=i)

frame2 = Frame(root, width=350, height=350)
lab1f2 = Label(frame2,font=("Arial",16,'bold'),text='Here is the list of all Your Expenses !!')
lab1f2.pack(pady=10)


tv2 = ttk.Treeview(frame2,columns=(1,2,3,4),show='headings',height='5',style="mystyle.Treeview")
tv2.column(1,anchor=CENTER,width=100)
tv2.column(2,anchor=CENTER,width=100)
tv2.column(3,anchor=CENTER,width=100)
tv2.column(4,anchor=CENTER,width=100)

tv2.pack()

tv2.heading(1,text='Item Name',anchor=CENTER)
tv2.heading(2,text='Price',anchor=CENTER)
tv2.heading(3,text='Category',anchor=CENTER)
tv2.heading(4,text='Date',anchor=CENTER)


menu_f2 = Button(frame2,text='Back to Menu',bg='yellow',font=("Algerian",13),command=menu2)
# menu_f2.place(x=105,y=260)
menu_f2.pack(side='bottom',pady=20)

# -------------------- FRAME 3 Update Entry  ------------------------


def update():
    d = tv3.item(tv3.focus())
    vl = (item.get(), pri.get(), cate.get(), dat.get(), d['values'][0])
    clr4()
    ql = "update expenditure " \
         "SET Item_Name = %s, Price= %s,Category=%s,Date=%s " \
         "WHERE Item_Name =%s"

    mycursor.execute(ql, vl)
    mydb.commit()
    display3()

def clr4():
    item.delete('0', 'end')
    pri.delete('0', 'end')
    cate.delete('0', 'end')
    dat.delete('0', 'end')
    item.focus_set()

def edit():
    clr4()
    d = tv3.item(tv3.focus())
    item.insert(0,d['values'][0])
    pri.insert(0,d['values'][1])
    cate.insert(0,d['values'][2])
    dat.insert(0,d['values'][3])

def display3():
    tv3.delete(*tv3.get_children())
    s = "select * from expenditure"
    mycursor.execute(s)
    records = mycursor.fetchall()
    # record_count = mycursor.rowcount
    for i in records:
        tv3.insert('','end',values=i)


frame3 = Frame(root, width=350, height=350)
lab1f3 = Label(frame3,text='Select a Record to Edit & Update !!',font=("Arial",13,'bold'))
lab1f3.pack(pady=10)


tv3 = ttk.Treeview(frame3,columns=(1,2,3,4),show='headings',height='3',style="mystyle.Treeview")
tv3.column(1,anchor=CENTER,width=100)
tv3.column(2,anchor=CENTER,width=100)
tv3.column(3,anchor=CENTER,width=100)
tv3.column(4,anchor=CENTER,width=100)

tv3.pack()

tv3.heading(1,text='Item Name',anchor=CENTER)
tv3.heading(2,text='Price',anchor=CENTER)
tv3.heading(3,text='Category',anchor=CENTER)
tv3.heading(4,text='Date',anchor=CENTER)
# -----------------------------
edt = Button(frame3,text='Edit',bg='lightgreen',font=("Algerian",11),command=edit)
edt.pack(side='top',pady=10)

item = Entry(frame3)
item.pack(side='top',pady=5)

pri = Entry(frame3)
pri.pack(side='top',pady=5)

cate = Entry(frame3)
cate.pack(side='top',pady=5)

dat = Entry(frame3)
dat.pack(side='top',pady=5)


upd = Button(frame3,text='Update',bg='lightblue',font=("Algerian",11),command=update)
upd.pack(pady=5)

menu_f3 = Button(frame3,text='Back to Menu',bg='yellow',font=("Algerian",13),command=menu3)
menu_f3.pack(side='bottom',pady=5)

# -------------------- FRAME 4 Delete Entry ------------------------

def del_entry():
    d = tv4.item(tv4.focus())
    val = d['values'][0]
    s = 'delete from expenditure where Item_Name=%s'
    mycursor.execute(s,(val,))
    mydb.commit()
    display4()

def display4():
    tv4.delete(*tv4.get_children())
    s = "select * from expenditure"
    mycursor.execute(s)
    records = mycursor.fetchall()
    # record_count = mycursor.rowcount
    for i in records:
        tv4.insert('','end',values=i)

frame4 = Frame(root, width=350, height=350)
lab1f4 = Label(frame4,text='Select a Record to Delete !!',font=("Arial",13,'bold'))
lab1f4.pack(pady=10)

tv4 = ttk.Treeview(frame4,columns=(1,2,3,4),show='headings',height='5',style="mystyle.Treeview")
tv4.column(1,anchor=CENTER,width=100)
tv4.column(2,anchor=CENTER,width=100)
tv4.column(3,anchor=CENTER,width=100)
tv4.column(4,anchor=CENTER,width=100)
tv4.pack()

tv4.heading(1,text='Item Name',anchor=CENTER)
tv4.heading(2,text='Price',anchor=CENTER)
tv4.heading(3,text='Category',anchor=CENTER)
tv4.heading(4,text='Date',anchor=CENTER)

dlt = Button(frame4,text='Delete Entry',bg='lightblue',font=("Algerian",11),command=del_entry)
dlt.pack(pady=20)

menu_f4 = Button(frame4,text='Back to Menu',bg='yellow',font=("Algerian",13),command=menu4)
menu_f4.pack(side='bottom',pady=20)

mainpage.pack()
root.mainloop()
