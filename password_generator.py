# Password Generator
from tkinter import *

import secrets

import pyperclip

from win10toast import ToastNotifier 


UPPER_CASE_ALPHABETS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

SPECIAL_CHARACTERS = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*',
                      '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', '\\', ':', ';', '<', ',', '>', '.', '?', '/']

NUMERICAL_CHARACTERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

select_uppercase = ''
select_special_char = ''
select_numerical_char = ''

var_uppercase = 0
var_special = 0
var_numerical = 0

resultant_password = ''


def mainWindow():
    global select_uppercase, select_special_char, select_numerical_char, var_numerical, var_special, var_uppercase, resultant_password
    root = Tk()
    root.config(bg="white")
    root.title("PASSWORD GENERATION AND MANAGEMENT SYSTEM")
    root.geometry("700x450+0+0")
    root.resizable(False, False)
    Tops = Frame(root, width=700, height=50, bd=16, relief="raise")
    Tops.pack(side=TOP)
    mainTitle = Label(Tops, text='Password Generator', borderwidth=1, relief="groove",
                      fg="steel blue", font=('arial', 15, 'bold'), bd=10, anchor='w')
    mainTitle.grid(row=0, column=0)
    LF = Frame(root, width=400, height=450, bd=16, relief="raise")
    LF.pack(side=LEFT)
    RF = Frame(root, width=300, height=450, bd=16, relief="raise")
    RF.pack(side=RIGHT)
    preferences = Label(LF, text='Select your preferences',
                        fg="steel blue", font=('arial', 12, 'bold'))
    preferences.grid(row=0, column=0, padx=10, pady=10)
    var_uppercase = IntVar()
    var_special = IntVar()
    var_numerical = IntVar()
    select_uppercase = Checkbutton(LF, text="Include Uppercase Alphabets", variable=var_uppercase,
                                   onvalue=1, offvalue=0).grid(row=1, column=0, padx=10, pady=10)
    select_special_char = Checkbutton(LF, text="Include Special Characters", variable=var_special,
                                      onvalue=1, offvalue=0).grid(row=2, column=0, padx=10, pady=10)
    select_numerical_char = Checkbutton(LF, text="Include Numerical Characters",
                                        variable=var_numerical, onvalue=1, offvalue=0).grid(row=3, column=0, padx=10, pady=10)
    resultant_password_txt = Label(
        LF, text='Resultant Password:', fg="steel blue", font=('arial', 11, 'bold'))
    resultant_password_txt.grid(row=4, column=0, padx=10, pady=10)
    resultant_password = Label(
        LF, text='gsgdhg2hh3h&@345', fg="steel blue", font=('arial', 11, 'bold'))
    resultant_password.grid(row=4, column=1, padx=10, pady=10)

    generate_btn = Button(RF, text="GENERATE RANDOM PASSWORD", command=generatePassword,
                          pady=6, bd=8, fg="steel blue", font=('arial', 10, 'bold'), width=26)
    generate_btn.grid(row=0, column=0, padx=5, pady=5)
    copy_btn = Button(RF, text="COPY TO CLIPBOARD", command=copyToClipboard,
                      pady=6, bd=8, fg="steel blue", font=('arial', 10, 'bold'), width=26)
    copy_btn.grid(row=1, column=0, padx=5, pady=5)
    reset_btn = Button(RF, text="RESET", command=resetPreferences, pady=6,
                       bd=8, fg="steel blue", font=('arial', 10, 'bold'), width=15)
    reset_btn.grid(row=2, column=0, padx=5, pady=5)
    password_manager = Button(RF, text="PASSWORD MANAGER", command=passwordManager,
                              pady=6, bd=8, fg="steel blue", font=('arial', 10, 'bold'), width=18)
    password_manager.grid(row=3, column=0, padx=5, pady=5)

    root.mainloop()


def generatePassword():
    if var_uppercase.get() == 1 and var_special.get() == 1 and var_numerical.get() == 1:
        resPassword = ''
        while True:
            get_random_uppercase = secrets.choice(UPPER_CASE_ALPHABETS)
            get_random_special = secrets.choice(SPECIAL_CHARACTERS)
            get_random_numerical = secrets.choice(NUMERICAL_CHARACTERS)

            resPassword += get_random_uppercase + get_random_special + get_random_numerical
            if len(resPassword) >= 8:
                break
        resultant_password.config(text=resPassword)


def copyToClipboard():
    textCopiedNotifier = ToastNotifier()
    pyperclip.copy(resultant_password.cget('text'))
    textCopiedNotifier.show_toast("Password Generator Notifier","Password Copied to Clipboard Successfully!",
    duration=10, threaded=True)


def resetPreferences():
    var_uppercase.set(0)
    var_special.set(0)
    var_numerical.set(0)
    resultant_password.config(text='gsgdhg2hh3h&@345')


def passwordManager():
    # new window
    pass


if __name__ == "__main__":
    mainWindow()
