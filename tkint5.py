import tkinter as tk

root=tk.Tk()

v=tk.IntVar()
def test():
    if v.get()==1:
        print("python selected")
    elif v.get()==2:
        print("perl selected")


b1=tk.Button(root,
                  text="find",
                   padx=40,
                   command=test)

l1=tk.Label(root,
              text="choose a programming language",
               justify=tk.LEFT,
                padx=20)
l1.pack()
l2=tk.Label(root,
                    text="",
                     justify=tk.CENTER,
                     font="20",
                     padx=20)
l1.pack()

r1=tk.Radiobutton(root,
                       text="python",
                        padx=20,
                         variable=v,
                         value=1)
r1.pack(anchor=tk.W)

r2=tk.Radiobutton(root,
                    text="perl",
                    padx=20,
                    variable=v,
                    value=2)
r2.pack(anchor=tk.W)

b1.pack(anchor=tk.W)
l2.pack(anchor=tk.W)

root.mainloop()
