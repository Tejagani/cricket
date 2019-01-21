import tkinter as tk

root=tk.Tk()

root.title("welcome to python and TK")

root.geometry('350x200')

lbl=tk.Label(root, text="hello")
lbl.grid(column=0, row=0)

txt=tk.Entry(root,width=10)
txt.grid(column=1,row=0)

def clicked():
    lbl.configure(text="hello mr."+txt.get())

btn=tk.Button(root,text="click me",command=clicked)
btn.grid(column=2, row=0)

root.mainloop()
