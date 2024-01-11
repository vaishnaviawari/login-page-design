from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    userEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmpasswordEntry.delete(0, END)
    check.set(0)
def connect_database():
    if emailEntry.get()=='' or userEntry.get()=='' or passwordEntry.get()==' ' or confirmpasswordEntry.get()==' ':
        messagebox.showerror('Error','All Fields Are Required')
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('Error','password mismatch')
    elif check.get()==0:
        messagebox.showerror('Error', 'Please Accept term & condition')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='',database='userdata')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue,Please Try Again')
            return

        try:
            query = 'CREATE DATABASE userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        query='select * from data where username=%s'
        mycursor.execute(query,(userEntry.get()))

        row=mycursor.fetchone()

        if row !=None:
            messagebox.showerror('Error','Username Already exists')

        else:
            query = 'insert into data(email, username, password) values (%s, %s, %s)'
            mycursor.execute(query, (emailEntry.get(), userEntry.get(), passwordEntry.get()))

            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is successfull')
            clear()
            signup_window.destroy()
            import signin

def login_page():
    signup_window.destroy()
    import signin

signup_window=Tk()
signup_window.title('signup Page')
signup_window.resizable(False,False)


# inserting background image
background=ImageTk.PhotoImage(file='bg.jpg')
bgLable=Label(signup_window,image=background)
bgLable.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

# creating heading
heading=Label(frame,text="CREATE AN ACCOUNT",font=('Microsoft yahei UI Light',18,"bold"),bg="white",fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)

# for email
emailLabel=Label(frame,text='Email',font=('Microsoft yahei UI light',10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=30,font=('Microsoft yahei UI light',10,'bold'),fg='white',bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

# for user
userLabel=Label(frame,text='User',font=('Microsoft yahei UI light',10,'bold'),bg='white',fg='firebrick1')
userLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

userEntry=Entry(frame,width=30,font=('Microsoft yahei UI light',10,'bold'),fg='white',bg='firebrick1')
userEntry.grid(row=4,column=0,sticky='w',padx=25)

#for password
passwordLabel=Label(frame,text='Password',font=('Microsoft yahei UI light',10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=30,font=('Microsoft yahei UI light',10,'bold'),fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

# for confirm password
confirmpasswordLabel=Label(frame,text='ConfirmPassword',font=('Microsoft yahei UI light',10,'bold'),bg='white',fg='firebrick1')
confirmpasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmpasswordEntry=Entry(frame,width=30,font=('Microsoft yahei UI light',10,'bold'),fg='white',bg='firebrick1',)
confirmpasswordEntry.grid(row=8,column=0,sticky='w',padx=25)

# check button
check=IntVar()
termsandconditions=Checkbutton(frame,text='i aggre to the term and condition',
                               font=('microrosoft yahei UI Light',10,'bold')
                               ,bg='white',fg='firebrick1',activebackground='white',activeforeground='firebrick1',cursor='hand2',variable=check)
termsandconditions.grid(row=9,column=0,pady=10,padx=15)

# for signpu button
signupButton=Button(frame,text='Signup',font=('Microsoft yahei UI light',16,'bold'),
                   fg='white',bg='firebrick1',activebackground='firebrick1',
                   activeforeground='white',
                   cursor='hand2',bd=0,width=17,command=connect_database)
signupButton.grid(row=10,column=
                  0,pady=10)

alreadyLabel=Label(frame,text="don,t have an account?",font=('Open sans',9,'bold'),bg='white',fg='firebrick1')
alreadyLabel.grid(row=11,column=0,sticky='w',padx=25,pady=(10,0))


loginButton=Button(frame,text='Log in',font=('Open sans',9,'bold underline'),
                   fg='blue',bg='white',activebackground='white',
                   activeforeground='blue',
                   cursor='hand2',bd=0,command=login_page)
loginButton.place(x=170,y=404)
signup_window.mainloop()