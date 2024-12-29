from tkinter import * 
import time

root = Tk()
root.geometry("300x250")
root.title("Counter")
h = 0

def loop():
    global h
    h += 1
    count_label.config(text=h)

def reset():
    global h
    h = 0
    count_label.config(text=h)

def show_time():
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=current_time)

# إنشاء العلامات
count_label = Label(root, text=h, bg="#F5E216", font=("Arial", 20))
count_label.place(x=120, y=5)

time_label = Label(root, bg="#F5E216", font=("Arial", 10))
time_label.place(x=120, y=50)

Button(root, text="Click", command=loop, width=15, height=2, bg="#FFA62F", activebackground="#F5E216", activeforeground="#FFA500", cursor="hand1").place(x=120, y=80)
Button(root, text="Reset", command=reset, width=15, height=2, bg="#FF6347", activebackground="#F5E216", activeforeground="#FFA500", cursor="hand1").place(x=120, y=130)
Button(root, text="Show Time", command=show_time, width=15, height=2, bg="#32CD32", activebackground="#F5E216", activeforeground="#FFA500", cursor="hand1").place(x=120, y=180)

root.mainloop()
