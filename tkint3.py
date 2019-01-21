import tkinter as tk
root=tk.Tk()
tk.Label(root,
               text="RED TEXT IN TIMES FONT",
               fg="red",
               font="times 18").pack()
tk.Label(root,
               text="green text in helvetica font",
               fg="light green",
               bg="dark green",
               font="helvetica 24 bold").pack()
tk.Label(root,
               text="blue text in verdana bold",
               fg="blue",
               bg="yellow",
               font="verdana 14 bold").pack()
root.mainloop()
