from tkinter import *
root = Tk()

def tambahcourse():
    print("course")
def deletcourse():
    print("deletcourse")
def tambahcontent():
    print("tambahcountent")
def deletcontent():
    print("deletcontent")
def tambahauthor():
    print("tambahauthor")
def deletauthor():
    print("deletauthor")



root.title("test dumbways")
canvas = Canvas(root,width=1300,height = 700)
canvas.pack()
label0 = Label(root,text="COURSE")
label0.config(font=("times",13))
canvas.create_window(210,50,window=label0)

label0 = Label(root,text="CONTENT")
label0.config(font=("times",13))
canvas.create_window(620,50,window=label0)

label0 = Label(root,text="AUTHOR")
label0.config(font=("times",13))
canvas.create_window(1030,50,window=label0)

ent = Entry(root)
canvas.create_window(290,100,window=ent)

ent1 = Entry(root)
canvas.create_window(290,150,window=ent1)

ent2 = Entry(root)
canvas.create_window(290,200,window=ent2)

ent3 = Entry(root)
canvas.create_window(290,250,window=ent3)

ent4 = Entry(root)
canvas.create_window(290,300,window=ent4)

ent5 = Entry(root)
canvas.create_window(290,350,window=ent5)

label0 = Label(root,text="id")
label0.config(font=("helventica",10))
canvas.create_window(185,100,window=label0)

label0 = Label(root,text="Nama ")
label0.config(font=("helventica",10))
canvas.create_window(180,150,window=label0)

label0 = Label(root,text="thumbnail ")
label0.config(font=("helventica",10))
canvas.create_window(175,200,window=label0)

label0 = Label(root,text="id_author ")
label0.config(font=("helventica",10))
canvas.create_window(175,250,window=label0)

label0 = Label(root,text="duration")
label0.config(font=("helventica",10))
canvas.create_window(175,300,window=label0)

label0 = Label(root,text="description")
label0.config(font=("helventica",10))
canvas.create_window(170,350,window=label0)
#####
ent6 = Entry(root)
canvas.create_window(700,100,window=ent6)

ent7 = Entry(root)
canvas.create_window(700,150,window=ent7)

ent8 = Entry(root)
canvas.create_window(700,200,window=ent8)

ent9 = Entry(root)
canvas.create_window(700,250,window=ent9)

ent10 = Entry(root)
canvas.create_window(700,300,window=ent10)

label0 = Label(root,text="id")
label0.config(font=("helventica",10))
canvas.create_window(585,100,window=label0)

label0 = Label(root,text="Nama ")
label0.config(font=("helventica",10))
canvas.create_window(580,150,window=label0)

label0 = Label(root,text="video link ")
label0.config(font=("helventica",10))
canvas.create_window(575,200,window=label0)

label0 = Label(root,text="type ")
label0.config(font=("helventica",10))
canvas.create_window(575,250,window=label0)

label0 = Label(root,text="id_course")
label0.config(font=("helventica",10))
canvas.create_window(575,300,window=label0)
#####
label0 = Label(root,text="id")
label0.config(font=("helventica",10))
canvas.create_window(985,100,window=label0)

label0 = Label(root,text="Nama ")
label0.config(font=("helventica",10))
canvas.create_window(980,150,window=label0)
ent11 = Entry(root)
canvas.create_window(1110,100,window=ent11)

ent12 = Entry(root)
canvas.create_window(1110,150,window=ent12)
######
buttonSub = Button(text='DELET', command=deletcourse, bg='green', fg='white', font=('helvetica', 9, 'bold'), width = 8)
canvas.create_window(200, 400, window=buttonSub)

buttonSub = Button(text='ADD', command=tambahcourse, bg='green', fg='white', font=('helvetica', 9, 'bold'), width = 8)
canvas.create_window(300, 400, window=buttonSub)
#####
buttonSub = Button(text='DELET', command=deletcontent, bg='green', fg='white', font=('helvetica', 9, 'bold'), width = 8)
canvas.create_window(600, 400, window=buttonSub)

buttonSub = Button(text='ADD', command=tambahcontent, bg='green', fg='white', font=('helvetica', 9, 'bold'), width = 8)
canvas.create_window(700, 400, window=buttonSub)
####
buttonSub = Button(text='DELET', command=deletauthor, bg='green', fg='white', font=('helvetica', 9, 'bold'), width = 8)
canvas.create_window(1000, 200, window=buttonSub)

buttonSub = Button(text='ADD', command=tambahauthor, bg='green', fg='white', font=('helvetica', 9, 'bold'), width = 8)
canvas.create_window(1100, 200, window=buttonSub)
root.mainloop()
