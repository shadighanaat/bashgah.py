# import all methods and classes from the tkinter 
# import mysql.connector classes
from tkinter import *
import mysql.connector

#Functions
def Add():

    name  = label_namefield.get()
    age = label_agefield.get()
    height = label_heightfield.get()
    wegiht = label_wegihtfield.get()
      
    print(name , age , height , wegiht)
   

def Clear():
    label_namefield.delete(0,END)

def Show():
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="parhamroham",
  database="bashgah"
)

  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM customers")

  myresult = mycursor.fetchall()

  for x in myresult:
   print(x)
   
# Create a window 
window = Tk()

window.title("Club members")

window.geometry()

#create labale name,age,height,wegiht
label_name = Label(window,text="name",font=50,bg="white")

label_age = Label(window,text="age",font=50,bg="white")

label_height = Label(window,text="height",font=50,bg="white")

label_wegiht = Label(window,text="wegiht",font=50,bg="white")

# create text entry box
label_namefield=Entry(window)

label_agefield=Entry(window)

label_heightfield=Entry(window)

label_wegihtfield=Entry(window)

#create three button
btn1 =Button(window,text="add a member",bg="yellow",fg="black",padx=40,pady=10,command=Add)

btn2 = Button(window,text="delete a member",bg="yellow",fg="black",padx=40,pady=10,command=Clear)

btn3 = Button(window,text="show the member",bg="yellow",fg="black",padx=40,pady=10,command=Show)

# the widgets at respective positions 
# in table like structure. 
label_name.grid(row=0)

label_age.grid(row=0, column=2)

label_height.grid(row=2,column=0)

label_wegiht.grid(row=2,column=2)

label_namefield.grid(row=0,column=1)

label_agefield.grid(row=0,column=3)

label_heightfield.grid(row=2,column=1)

label_wegihtfield.grid(row=2,column=3)

btn1.grid(row=3,column=0)

btn2.grid(row=3,column=2)

btn3.grid(row=3,column=4)

#start the window 
window.mainloop()     
