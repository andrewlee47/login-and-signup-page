from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import os


mysql_username = os.environ.get('user')
pass_word = os.environ.get('password')

if mysql_username is not None and pass_word is not None:
    pass

else:
    print("Please set your database login environment variable. ")


#code for functionality


def LOGIN_USER():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Input Your login credential')
    else:
        try:
            conn = pymysql.connect(host='localhost',user=mysql_username, password=pass_word)
            my_cursor = conn.cursor()
        except:
            messagebox.showerror('Error', 'Connection fail Try again')
            return

        query = 'use userdata'
        my_cursor.execute(query)
        query = 'select * from data where username = %s and password = %s'
        my_cursor.execute(query, (usernameEntry.get(), passwordEntry.get()))

        checking_details = my_cursor.fetchone()


        if checking_details is None:
            messagebox.showerror('Error', 'Invalid Username or Password')

        else:
            messagebox.showinfo('Welcome', 'Login is Successful')



def signup_page():
    login_win.destroy()
    import signUp


def hide():
    open_eye.config(file='close eye.png')
    passwordEntry.config(show='*')
    eye_button.config(command=show)


def show():
    open_eye.config(file='open eye.png')
    passwordEntry.config(show='')
    eye_button.config(command=hide)




def user_click(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)


def pass_click(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)


def forget_Pass():
    def change_password():
        if User_name_entry.get() == '' or New_pass_entry.get() == '':
            messagebox.showerror('Error', 'All field required')
        elif New_pass_entry.get() != confirm_pass_entry.get():
            messagebox.showerror('Error', 'Password mismatched')
        else:
            conn = pymysql.connect(host='localhost', user='root', password='sucklex', database='userdata')
            my_cursor = conn.cursor()
            query = 'select * from data where username=%s'
            my_cursor.execute(query, (User_name_entry.get()))
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror('Error', 'Username not found')
            else:
                query = 'update data set password=%s where username=%s'
                my_cursor.execute(query, (New_pass_entry.get(), User_name_entry.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo('Successful', 'Password reset, kindly login')
                window.destroy()

    window = Toplevel()
    window.title('Reset Password')

    window.geometry('600x750')
    window.resizable(0, 0)

    back_ground_img = ImageTk.PhotoImage(file='pexels-photo-11592804.jpeg')

    back_ground_label = Label(window, image=back_ground_img)
    back_ground_label.grid(row=0, column=0)

    reset_label = Label(window, text='RESET PASSWORD', bd=0, bg='light coral',
                        font=('STIX', 30, 'bold'), fg='medium violet red')
    reset_label.place(x=120, y=20)

    User_Name = Label(window, text='Username', bd=0, bg='light coral',
                      font=('STIX', 21, 'bold',), fg='medium violet red')
    User_Name.place(x=30, y=120)

    User_name_entry = Entry(window, bd=0, width=30, bg='seashell4',
                            font=('STIX', 23), fg='black')
    User_name_entry.place(x=30, y=175)

    user_frame = Frame(window, width=512, height=3, bg='medium violet red')
    user_frame.place(x=30, y=210)

    New_pass = Label(window, text='New Password', bd=0, bg='light coral',
                     font=('STIX', 21, 'bold',), fg='medium violet red')
    New_pass.place(x=30, y=245)

    New_pass_entry = Entry(window, bd=0, width=30, bg='seashell4',
                           font=('STIX', 23), fg='black')
    New_pass_entry.place(x=30, y=300)

    new_frame = Frame(window, width=512, height=3, bg='medium violet red')
    new_frame.place(x=30, y=335)

    confirm_pass = Label(window, text='Confirm Password', bd=0, bg='light coral',
                         font=('STIX', 21, 'bold',), fg='medium violet red')
    confirm_pass.place(x=30, y=375)

    confirm_pass_entry = Entry(window, bd=0, width=30, bg='seashell4',
                               font=('STIX', 23), fg='black')
    confirm_pass_entry.place(x=30, y=435)

    confirm_frame = Frame(window, width=512, height=3, bg='medium violet red')
    confirm_frame.place(x=30, y=470)

    submit_button = Button(window, text='Submit', font=('STIX', 30, 'bold'),
                           bg='medium violet red', fg='seashell4', activebackground='medium violet red',
                           activeforeground='seashell4', width=20, command=change_password, cursor='hand2')
    submit_button.place(x=50, y=550)

    window.mainloop()

#GUI code

login_win = Tk()
login_win.geometry("600x750+50+50")
login_win.resizable(0,0)
login_win.title("LOGIN")




bgImg = ImageTk.PhotoImage(file='pexels-photo-11592804.jpeg')

bgLabel = Label(login_win,image=bgImg)
bgLabel.grid(row=0, column=0)

heading = Label(login_win, text="USER LOGIN",font=('Courier',30,'bold'),
                fg="black", bg="pale violet red",activebackground='seashell4')
heading.place(x=165, y=140)


#Code for Entering username
usernameEntry = Entry(login_win, width=30,font=('Garuda',12,),
                      bd=0, bg='white', fg="black")
usernameEntry.place(x=150, y=230)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_click)


Frame1 = Frame(login_win, width=273, height=2, bg='seashell4')
Frame1.place(x=150, y=250)

#Code  for entering password

passwordEntry = Entry(login_win, width=30,font=('Garuda', 12,),
                      bd=0, bg='white',fg="black")
passwordEntry.place(x=150, y=290)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', pass_click)

Frame2 = Frame(login_win, width=273, height=2, bg='seashell4')
Frame2.place(x=150, y=310)

#Show password button and eye button

open_eye = PhotoImage(file='open eye.png')
eye_button = Button(login_win,height=15, image=open_eye, bd=0,bg='white',
                    activebackground='white',cursor='hand2',command=hide)
eye_button.place(x=395, y=290)


#FORGET BUTTON CODE


forget_button = Button(login_win, text="Forgot Password?", bd=0,bg='seashell4'
                       ,cursor='hand2',activeforeground='seashell4', activebackground='seashell4',
                       command=forget_Pass)
forget_button.place(x=315, y=325)


Login_Button = Button(login_win, text='Login', bg='seashell4',font=('Courier', 25, 'bold'),
                      width=13,bd=0, activebackground='pale violet red', activeforeground='black',cursor='hand2', command=LOGIN_USER)
Login_Button.place(x=153, y=400)

#CODE FOR ---OR-- LABEL

orLabel = Label(login_win, text='------ OR ------', font=('Courier',20,'italic','bold'),
                bg='pale violet red')
orLabel.place(x=159, y=490)

#CODE FOR FACEBOOK, GOOGLE AND TWITTER LABEL

fb_logo = PhotoImage(file='facebook.png')
fb_label = Label(login_win, image=fb_logo, bg='seashell4')
fb_label.place(x=170, y=570)


tw_logo = PhotoImage(file='twitter.png')
tw_label = Label(login_win, image=tw_logo, bg='seashell4')
tw_label.place(x=280, y=570)


gog_logo = PhotoImage(file='google(1).png')
gog_label = Label(login_win, image=gog_logo, bg='seashell4')
gog_label.place(x=380, y=570)


orLabel = Label(login_win, text="Don't have an account?", font=('Courier',10,'bold'),
                bg='seashell4', fg='black')
orLabel.place(x=70, y=700)


#NEW ACCOUNT BUTTON


New_Button = Button(login_win, text='Click here', bg='red', fg='black', font=('Courier', 14, 'bold','underline'),
                    activebackground='red',activeforeground='brown', bd=0, cursor='hand2', command=signup_page)
New_Button.place(x=305, y=695)


login_win.mainloop()
