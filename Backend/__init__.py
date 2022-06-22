from .login import login
from .signup import signUp
from .CreateEvent import new_event

def Login(uname, pswd):
    return login(uname, pswd)

def SignUp(uname, pswd):
    return signUp(uname, pswd)

def New_Event(userID, Date, Title, Event):
    new_event(userID, Date, Title, Event)

if __name__ == "__main__":
    print(Login("Sid", "Sid7777"))