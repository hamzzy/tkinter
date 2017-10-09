from Tkinter import *
import ttk
import time
import sqlite3
import random

root=Tk()




tabControl = ttk.Notebook(root) # Create Tab Control
tab1 = ttk.Frame(tabControl) # Create a tab
tabControl.add(tab1, text='FARM RECORD') # Add the tab
tabControl.pack(expand=1, fill="both")



def submit():
   var1=name.get()
   var2=well.get()
   var3= finance.get()
   var4= money.get()
   a=time.asctime()
   b=random.randint(1,1000)
   #var5=observation.get()
   tree.insert('',0,text=b,values=(var1,str(var2),str(var3),var4,a))
   conn=sqlite3.connect('dell.db')
   c=conn.cursor()
    
   
   #c.execute('CREATE TABLE account(id primary key ,cost CHAR(50),debit INT(50),credit INT(50),farm CHAR(200),datestamp TEXT)')
   c.execute('INSERT INTO account (cost,debit,credit,farm,datestamp)VALUES(?,?,?,?,?)',(var1,var2,var3,var4,a))
    
    
   conn.commit()
   conn.close()
  # print(a)
   
   

 
    

name=StringVar()
well=IntVar()
finance=IntVar()
money=StringVar()
#observation=StringVar()
frame = Frame(tab1, relief=RAISED, borderwidth=10)
frame.pack(fill=BOTH ,expand=1)


Label(frame,text="COST:",relief=RAISED).grid(row=0,padx=5)
Label(frame,text="DEBIT:",relief=RAISED).grid(row=1,padx=5)
Label(frame,text="CREDIT:",relief=RAISED).grid(row=2,padx=5)
Label(frame,text="FARM:",relief=RAISED).grid(row=3,padx=5)

e1=Entry(frame,bd=6,width=70,textvariable=name).grid(row=0,column=1,padx=10)
e2=Entry(frame,bd=6,width=70,textvariable=well).grid(row=1,column=1,pady=20,)
e3=Entry(frame,bd=6,width=70,textvariable=finance).grid(row=2,column=1,pady=20,)
e4=Entry(frame,bd=6,width=70,textvariable=money).grid(row=3,column=1)

w=Text(frame,height=20,width=70,relief=GROOVE).grid(column=1,row=6,pady=15)



btn1=Button(frame,text="SUBMIT",relief=RAISED,width=40,height=2,bd=6,command=submit).grid(column=1,row=7)


tree=ttk.Treeview(frame,height=10)
tree['columns']=('one','two','three','four','five')
tree.heading('one',text="COST")
tree.heading('two',text="DEBIT")
tree.heading('three',text="CREDIT")
tree.heading('four',text="FARM")
tree.heading('five',text="TIME")
tree.grid(row=8,column=1,pady=5)




tab2 = ttk.Frame(tabControl) # Create a tab
tabControl.add(tab2, text='FARM DAIRY') # Add the tab
tabControl.pack(expand=TRUE, fill=BOTH)
frame1 = Frame(tab2, relief=RIDGE, borderwidth=2)
frame1.pack(fill=BOTH,expand=1)
def recall():
   
   
   conn=sqlite3.connect('dell.db')
   c=conn.cursor()
   
    
   #c.execute('CREATE TABLE account(cost CHAR(50),debit INT(50),credit INT(50),farm CHAR(200))')
  # a= c.execute('INSERT INTO account (cost,debit,credit,farm)VALUES(?,?,?,?)',(var1,var2,var3,var4))
   query=c.execute("SELECT * FROM account")
   #c.fetchall()
   for row in query.fetchall():
      tree.insert('',0,values=(row))
    
   conn.commit()
   conn.close()
def delete():
   var1=name.get()
   var2=well.get()
   var3= finance.get()
   var4= money.get()
   a=time.asctime()
   conn=sqlite3.connect('dell.db')
   c=conn.cursor()
   
    
   #c.execute('CREATE TABLE account(cost CHAR(50),debit INT(50),credit INT(50),farm CHAR(200))')
  # a= c.execute('INSERT INTO account (cost,debit,credit,farm)VALUES(?,?,?,?)',(var1,var2,var3,var4))
   query=c.execute('delete from account')

 #c.fetchall()
   for query in tree.get_children():
       tree.delete(query)
    
   conn.commit()
   conn.close()
   


tree=ttk.Treeview(frame1,height=30)
tree['columns']=('one','two','three','four','five')
tree.heading('one',text="COST")
tree.heading('two',text="DEBIT")
tree.heading('three',text="CREDIT")
tree.heading('four',text="FARM")
tree.heading('five',text="TIME")
tree.grid(row=0,column=1,pady=5)
btn2=Button(frame1,text="get from db",width=50,command=recall).grid(row=2,column=1)
btn2=Button(frame1,text="delete",width=50,command=delete).grid(row=3,column=1)




tab3 = ttk.Frame(tabControl) # Create a tab
tabControl.add(tab3, text='GRAPH') # Add the tab
tabControl.pack(expand=1, fill=BOTH)


tab4 = ttk.Frame(tabControl) # Create a tab
tabControl.add(tab4, text='DATABASE') # Add the tab
tabControl.pack(expand=1, fill=BOTH)

root.mainloop()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
