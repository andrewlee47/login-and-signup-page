from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import os

signUp = Tk()
signUp.geometry('600x750')
signUp.title('SIGN UP')
signUp.resizable(0, 0)




mysql_username = os.environ.get('user')
pass_word = os.environ.get('password')

if mysql_username is not None and pass_word is not None:
    pass

else:
    print("Please set your database login environment variable. ")

# Function to connect to database


def clear():
    email_entry.delete(0, END)
    user_entry.delete(0, END)
    pass_entry.delete(0, END)
    confirm_pass.delete(0, END)
    check.set(0)


def connect_database():
    if email_entry.get() == '' or pass_entry.get() == '' or confirm_pass.get() == '':
        messagebox.showerror('Error', 'All fields are required')

    elif pass_entry.get() != confirm_pass.get():
        messagebox.showerror('Error', 'Password not match')

    elif check.get() == 0:
        messagebox.showerror('Error', 'Accept terms & Conditions')

    else:
        try:
            conn = pymysql.connect(host='localhost', user=mysql_username, password=pass_word)
            my_cursor = conn.cursor()
        except:
            messagebox.showerror('Error', 'Error connecting to database')
            return
        try:
            query = 'create database userdata'
            my_cursor.execute(query)
            query = 'use userdata'
            my_cursor.execute(query)
            query = "Create Table data(id int auto_increment primary key not null, email varchar(50), username varchar(50), password varchar(20))"
            my_cursor.execute(query)
        except:
            my_cursor.execute('use userdata')

        query = 'select * from data where username = %s'
        my_cursor.execute(query, (user_entry.get()))



        checking_username = my_cursor.fetchone()


        if checking_username is not None:
            messagebox.showerror('Error', 'Username Already exist')

        else:

            query = 'insert into data(email, username, password) values(%s,%s,%s)'
            my_cursor.execute(query, (email_entry.get(), user_entry.get(), pass_entry.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('Successful', 'Registered')
            clear()
            signUp.destroy()
            import login


# FUNCTIONALITY CODE FOR Log in


def login_page():
    signUp.destroy()
    import login



#setting up the background image


bck_img = ImageTk.PhotoImage(file='pexels-photo-11592804.jpeg')

bck_label = Label(signUp, image=bck_img)
bck_label.place(x=0, y=0)

new_acct = Label(signUp, text='CREATE AN ACCOUNT', font=('Courier', 30, 'bold'),
                 bg='seashell4', fg='pale violet red')
new_acct.place(x=90, y=10)


#Email label and entry

email_label = Label(signUp, text='Email', font=('Courier', 20, 'italic', 'bold'),
                    bg='seashell4', fg='black')
email_label.place(x=15, y=100)

email_entry = Entry(signUp, bg='pale violet red', width=35, font=('Courier', 20))
email_entry.place(x=15, y=150)


#User label and entry

user_label = Label(signUp, text='Username', font=('Courier', 20, 'italic', 'bold'),
                   bg='seashell4', fg='black')
user_label.place(x=15, y=200)

user_entry = Entry(signUp, bg='pale violet red', width=35, font=('Courier', 20))
user_entry.place(x=15, y=250)


#Pasdsword label and entry


pass_label = Label(signUp, text='Password', font=('Courier', 20, 'italic', 'bold'),
                   bg='seashell4', fg='black')
pass_label.place(x=15, y=300)

pass_entry = Entry(signUp, bg='pale violet red', width=35, font=('Courier', 20))
pass_entry.place(x=15, y=350)

confirm_pass = Label(signUp, text='Confirm Password', font=('Courier', 20, 'italic', 'bold'),
                     bg='seashell4', fg='black')
confirm_pass.place(x=15, y=400)

confirm_pass = Entry(signUp, bg='pale violet red', width=35, font=('Courier', 20))
confirm_pass.place(x=15, y=450)


#Terms and condition


check = IntVar()
terms_condition = Checkbutton(signUp, bd=0, text='I agree to the Terms & Conditions', bg='seashell4',
                              activebackground='seashell4', font=('Courier', 15), variable=check)
terms_condition.place(x=15, y=500)

#Sign up button

sign_up = Button(signUp, text='SIGN UP', bg='pale violet red', font=('Courier', 25, 'bold'),
                 width=15, bd=0, activebackground='pale violet red',
                 activeforeground='black', cursor='hand2', command=connect_database)
sign_up.place(x=153, y=550)

already_signup = Label(signUp, bd=0, text='Already have an account?', bg='seashell4', font=('Courier', 15, 'bold'))
already_signup.place(x=100, y=650)


#Login button
login_button = Button(signUp, text='Log in', bg='red', font=('Courier', 14, 'bold', 'underline'),
                      bd=0, activebackground='red', activeforeground='black', cursor='hand2', command=login_page)
login_button.place(x=410, y=648)

signUp.mainloop()
