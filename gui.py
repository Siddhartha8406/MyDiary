from tkinter import Tk, Button, Entry, Label

root = Tk()
root.geometry("500x450")
root.configure(bg="#1263AC")

def dest():
    pass

uname=""
pswd=""

#---User Name---
l1=Label(root, text="Username", font="size=15", background="#105695")
e1=Entry(root, textvariable=uname, font="size=15")
l1.place(rely=0.4, relx=0.23)
e1.place(rely=0.4, relx=0.40)

#---Password---
l2=Label(root, text="Password", font="size=15", background="#105695")
e2=Entry(root, textvariable=uname, font="size=15")
l2.place(rely=0.48, relx=0.23)
e2.place(rely=0.48, relx=0.40)

#---Login Button---
b1=Button(root, text="Sign In", font="size=18", background="#105695", borderwidth=1.5)
b1.place(rely=0.55, relx=0.4)

#---Forgot Password---
ForgotPassword=Button(root, text="Forgot Password", background="#1263AC",border=0, command=dest)
ForgotPassword.place(rely=0.7, relx=0.4)

#---Create New---
ForgotPassword=Button(root, text="Create New Account", background="#1263AC",border=0, command=dest)
ForgotPassword.place(rely=0.75, relx=0.38)
root.mainloop()