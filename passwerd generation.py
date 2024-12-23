from tkinter import*
from random import randint
root=Tk()
root.title('password genyrator') 
root.geometry("500x300")


#lable frame

def new_pass():
    pw_entry.delete(0, END )

    pw_length=int(my_entry.get())

    my_password=""

    for x in range(pw_length):
        my_password +=chr(randint(33,126))

    pw_entry.insert(0,my_password)    

def clipper():
    root.clipboard_clear()

    root.clipboard_append(pw_entry.get())

If=LabelFrame(root,text="how many characters")
If.pack(pady=20)

my_entry=Entry(If,font=("Helvatica",24))
my_entry.pack(padx=20,pady=20)

pw_entry=Entry(root,font=("Helvatica",24),bd=0,bg="systembuttonface")
pw_entry.pack(pady=20)

my_frame= Frame(root)
my_frame.pack(pady=20)

my_button=Button(my_frame,text="generate strong password",command=new_pass)
my_button.grid(row=0,column=0,pady=10)

clip_button=Button(my_frame,text=" Copy ",command=clipper)
clip_button.grid(row=0,column=1,padx=10)
root.mainloop()