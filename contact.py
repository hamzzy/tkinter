from Tkinter import *
import ttk
win = Tk() # Create instance
win.title("Python GUI") # Add a title
tabControl = ttk.Notebook(win) # Create Tab Control
tab1 = ttk.Frame(tabControl) # Create a tab
tabControl.add(tab1, text='Tab 1') # Add the tab
tabControl.pack(expand=1, fill="both") # Pack to make visible



def post():
    val=vul.get()
    fall=fell.get()
    well=feel.get()
    listbox.insert(END,val+" "+well+"---------"+"+234"+str(fall))
    listbox.delete(END,val+" "+well+"---------"+"+234"+str(fall))








fell=IntVar()
vul=StringVar()
feel=StringVar()

win.config(background="orange")
lb=Label(tab1,text="NAME:").pack()
e1=Entry(tab1,textvariable=vul,width=50).pack()

lb=Label(tab1,text="SURNAME:").pack()
e3=Entry(tab1,textvariable=feel,width=50).pack()

lb=Label(tab1,text="NAME:").pack()
e2=Entry(tab1,textvariable=fell,width=50).pack()
btn=Button(tab1,text="drop",command=post).pack()
scroll=Scrollbar(tab1)
scroll.pack(side=RIGHT,fill=Y)

listbox=Listbox(tab1)
listbox.config(yscrollcommand=scroll.set)
listbox.pack(expand=YES,fill=BOTH)
scroll.config(command=listbox.yview)




tab2 = ttk.Frame(tabControl) # Create a tab
tabControl.add(tab2, text='Tab 1') # Add the tab
tabControl.pack(expand=1, fill="both") # Pack to ma

win.mainloop()
