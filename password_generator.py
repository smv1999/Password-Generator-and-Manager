# Password Generator
from tkinter import *

UPPER_CASE_ALPHABETS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',\
     'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

SPECIAL_CHARACTERS = ['~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}',']','|','\\',':',';','<',',','>','.','?','/']

NUMERICAL_CHARACTERS = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']

def mainWindow():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("PASSWORD GENERATION AND MANAGEMENT SYSTEM")
    root.geometry("700x350+0+0")
    Tops=Frame(root,width=700,height=50,bd=16,relief="raise")
    Tops.pack(side=TOP)
    mainTitle = Label(Tops, text='Password Generator', borderwidth=2, relief="groove", fg="steel blue",font=('arial',15,'bold'), bd=10, anchor='w') 
    mainTitle.grid(row=0, column=0)
    LF=Frame(root,width=400,height=350,bd=16,relief="raise")
    LF.pack(side=LEFT)
    RF=Frame(root,width=300,height=350,bd=16,relief="raise")
    RF.pack(side=RIGHT)
    preferences = Label(LF, text='Select your preferences',fg="steel blue",font=('arial',12,'bold'))
    preferences.grid(row=0, column=0)
    Checkbutton(LF, text="Include Uppercase Alphabets", variable=StringVar(), onvalue=1, offvalue=0).grid(row=1, column=0, padx=10, pady=10)
    Checkbutton(LF, text="Include Special Characters", variable=StringVar(), onvalue=1, offvalue=0).grid(row=2, column=0, padx=10, pady=10)
    Checkbutton(LF, text="Include Numerical Characters", variable=StringVar(), onvalue=1, offvalue=0).grid(row=3, column=0, padx=10, pady=10)
    resultant_password_txt = Label(LF, text='Resultant Password:',fg="steel blue",font=('arial',12,'bold'))
    resultant_password_txt.grid(row=4, column=0)
    resultant_password = Label(LF, text='gsgdhg2hh3h&@345',fg="steel blue",font=('arial',12,'bold'))
    resultant_password.grid(row=4, column=1)
    
    generate_btn = Button(RF, text="GENERATE", command=generatePassword, pady=8,bd=8,fg="steel blue",font=('arial',13,'bold'),width=15)
    generate_btn.grid(row=0, column=0, padx=10, pady=10)
    reset_btn = Button(RF, text="RESET", command=resetPreferences, pady=8,bd=8,fg="steel blue",font=('arial',13,'bold'),width=15)
    reset_btn.grid(row=1, column=0, padx=10, pady=10)
    password_manager = Button(RF, text="PASSWORD MANAGER", command=passwordManager, pady=8,bd=8,fg="steel blue",font=('arial',13,'bold'),width=18)
    password_manager.grid(row=2, column=0, padx=10, pady=10)
 
    root.mainloop()

def generatePassword():
    pass
def resetPreferences():
    pass
def passwordManager():
    pass

if __name__ == "__main__":
    mainWindow()
