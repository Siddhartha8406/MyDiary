from tkinter import Tk, PhotoImage, Label, Entry, StringVar, Button, font

class main:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x450')
        self.root.configure(bg="#1263AC")
        self.uname = StringVar
        self.userid = StringVar

        img = PhotoImage(file=r"images/logo.png")
        label = Label(self.root, image=img, background="#1263AC")
        label.place(relx=0.2, rely=0.15)

        l1=Label(self.root, text="Username", font="size=20", background="#105695")
        e1=Entry(self.root, textvariable=self.uname, font="size=20")
        l1.place(rely=0.37, relx=0.23)
        e1.place(rely=0.37, relx=0.40)

        #---Password---
        l2=Label(self.root, text="User ID", font="size=20", background="#105695")
        e2=Entry(self.root, textvariable=self.userid, font="size=20")
        l2.place(rely=0.48, relx=0.25)
        e2.place(rely=0.48, relx=0.40)

        #---Login Button---
        b1=Button(self.root, text="Change Password", font="size=18", background="#105695", borderwidth=0.5, activebackground="#12395D")#, command=login)
        b1.place(rely=0.58, relx=0.34)

        self.root.mainloop()

start = main()