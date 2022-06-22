from tkinter import Tk, Button, Entry, Label, Frame, PhotoImage, StringVar
from Backend import Login

root = Tk()
root.geometry("500x450")
root.configure(bg="#1263AC")

uname=StringVar()
pswd=StringVar()
def login():
    user_name = uname.get()
    password = pswd.get()
    login_info = Login(user_name, password)
    if login_info[0]:
        print(f"Login Successful, user id={login_info[1]}")
        root.destroy()
    else:
        wrong = Label(root, text="Wrong Credientials. Try again", background="#1263AC", foreground='red', font="size=15")
        wrong.place(relx=0.28, rely=0.625)
        ForgotPassword.place(rely=0.675, relx=0.35)     
        CreateNew.place(rely=0.73, relx=0.32)



def SignUp():
    pass

def forgot_password():
    pass

#---Logo---
img = PhotoImage(file=r"images/logo.png")
label = Label(root, image=img, background="#1263AC")
label.place(relx=0.2, rely=0.15)

#---User Name---
l1=Label(root, text="Username", font="size=15", background="#105695")
e1=Entry(root, textvariable=uname, font="size=15")
l1.place(rely=0.4, relx=0.23)
e1.place(rely=0.4, relx=0.40)

#---Password---
l2=Label(root, text="Password", font="size=15", background="#105695")
e2=Entry(root, textvariable=pswd, font="size=15")
l2.place(rely=0.48, relx=0.23)
e2.place(rely=0.48, relx=0.40)

#---Login Button---
b1=Button(root, text="Log In", font="size=18", background="#105695", borderwidth=0.5, activebackground="#12395D", command=login)
b1.place(rely=0.55, relx=0.42)

#---Forgot Password---
ForgotPassword=Button(root, text="Forgot Password", background="#1263AC",border=0, font="size=18", command=forgot_password, activebackground="#1A7BD3")
ForgotPassword.place(rely=0.64, relx=0.35)

#---Create New---
CreateNew=Button(root, text="Create New Account", background="#1263AC",border=0, font="size=18", command=SignUp, activebackground="#1A7BD3")
CreateNew.place(rely=0.70, relx=0.32)

root.mainloop()