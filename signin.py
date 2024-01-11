from tkinter import *
import tkinter.messagebox
import messagebox
from PIL import ImageTk
import signup
import tk
import pymysql

# function def
def delete_account():

    window1 = Tk()

    window1.title('Delete Account')

    img = ImageTk.PhotoImage(Image.open('bg2.jpg'))

    imglable = Label(window1,image=img).grid(row=0,column=0)














    window1.mainloop()




def forget_pass():
    def change_password():
        if user_entry.get()==' ' or Newpassword_entry.get()==' ' or confirmpass_entry.get()==' ':
            messagebox.showerror('Error','All Fields Are Required')
        elif Newpassword_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Error', 'password and confirm pasword are not matching')
        else:
            con = pymysql.connect(host='localhost', user='root', password='', database='userdata')
            mycursor =con.cursor()
            query ='select * from data where username=%s'
            mycursor.execute(query,(user_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect username')
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(Newpassword_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset,please login with new passwore')
                
    window =Toplevel()
    window.title('change password')
    #
    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bgLable = Label(window, image=bgPic)
    bgLable.grid(row=0, column=0, sticky="nsew")

    heading_lable =Label(window, text="RESET PASSWORD", font=('arial', 18, "bold"),
                         bg="white", fg='firebrick1')
    heading_lable.place(x=480, y=60)

    userlable = Label(window, text="Username", font=('arial', 12, "bold"),
                      bg="white", fg='firebrick1')
    userlable.place(x=470, y=130)

    user_entry=Entry(window,width=25,fg='firebrick1',font=('arial',11,'bold'),bd=0)
    user_entry.place(x=470,y=160)
    Frame(window,width=250,height=2,bg='firebrick1').place(x=470,y=180)

    Newpasslable = Label(window, text="New password", font=('arial', 12, "bold"),
                      bg="white", fg='firebrick1')
    Newpasslable.place(x=470, y=210)

    Newpassword_entry=Entry(window,width=25,fg='firebrick1',font=('arial',11,'bold'),bd=0)
    Newpassword_entry.place(x=470,y=240)
    Frame(window,width=250,height=2,bg='firebrick1').place(x=470,y=260)

    confirmpasslable = Label(window, text="New password", font=('arial', 12, "bold"),
                         bg="white", fg='firebrick1')
    confirmpasslable.place(x=470, y=290)


    confirmpass_entry = Entry(window, width=25, fg='firebrick1', font=('arial', 11, 'bold'), bd=0)
    confirmpass_entry.place(x=470, y=320)
    Frame(window, width=250, height=2, bg='firebrick1').place(x=470, y=340)

    submitBotton = Button(window, text='Submit', font=('open sans', 16, 'bold'),
                         fg='white', bg='firebrick1', activebackground='firebrick1',
                         activeforeground='white',
                         cursor='hand2', bd=0, width=19,command=change_password)
    submitBotton.place(x=470, y=390)



    window.mainloop()





def login_user():
    if usernameEntry.get()==' ' or passwordEntry.get()==' ':
        messagebox.showerror('Error','All Fields Are Recuired')

    else:
        try:
            con=pymysql.connect(host='localhost', user='root', password='', database='userdata')
            mycursor = con.cursor()

        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid user name or password')
        else:
            messagebox.showinfo('Welcome','Login is sucessful')



def signup_page():
   root.destory()



def user_enter(event):
    if usernameEntry.get()=='username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if usernameEntry.get()=='password':
        usernameEntry.delete(0,END)


def hide():
    openeye.config(file="closeye.png")
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file="openeye.png")
    passwordEntry.config(show='')
    eyeButton.config(command=hide)







root=Tk()

root.geometry('990x660+50+50')
bgImage=ImageTk.PhotoImage(file="bg.jpg")

bgLable=Label(root,image=bgImage)
bgLable.place(x=0,y=0)





heading=Label(root,text="USER LOGIN",font=('Microsoft yahei UI Light',23,"bold"),bg="white",fg='firebrick1')
heading.place(x=605,y=120)
# entry for user
usernameEntry=Entry(root,width=25,font=('Microsoft yahei UI Light',11,"bold"),bd=0,fg="firebrick1")
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,"username")
usernameEntry.bind("<FocusIn>",user_enter)

# entry for password
passwordEntry=Entry(root,width=25,font=('Microsoft yahei UI Light',11,"bold"),bd=0,fg="firebrick1")
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,"password")
usernameEntry.bind("<FocusIn>",password_enter)
# frame for user
frame1=Frame(root,width=250,height=2,bg='firebrick1').place(x=580,y=222)
# frame for password
frame2=Frame(root,width=250,height=2,bg='firebrick1').place(x=580,y=282)


# openeye & closeeye
openeye=PhotoImage(file="openeye.png")
eyeButton=Button(root,image=openeye,bd=0,bg='white',activebackground="white",
                 cursor="hand2",command=hide)
eyeButton.place(x=800,y=255)


forgetButton=Button(root,text='Forget password?',
                    bd=0,bg='white',
                    activebackground="white",
                    cursor="hand2",
                    font=('Microsoft yahei UI Light',9,"bold"),fg='firebrick1',activeforeground='firebrick1',command=forget_pass)
forgetButton.place(x=715,y=295)

deleteButton = Button(root, text='Delete Account.', font=('Microsoft yahei UI Light',9 , 'bold'),
                      fg='firebrick1', bg='white', activebackground='white',
                      activeforeground='firebrick1',
                      cursor='hand2', bd=0,command=delete_account)
deleteButton.place(x=715, y=315)

loginBotton=Button(root,text='login',font=('open sans',16,'bold'),
                   fg='white',bg='firebrick1',activebackground='white',
                   activeforeground='firebrick1',
                   cursor='hand2',bd=0,width=19,command=login_user)
loginBotton.place(x=578,y=350)

orLabel=Label(root,text='---------------OR---------------',font=('Open sans',16),fg='firebrick1')
orLabel.place(x=583,y=400)



facebook_logo=PhotoImage(file='facebook.png')
fbLable=Label(root,image=facebook_logo,bg='white')
fbLable.place(x=640,y=440)

google_logo=PhotoImage(file='google.png')
googleLable=Label(root,image=google_logo,bg='white')
googleLable.place(x=690,y=440)

twitter_logo=PhotoImage(file='twitter.png')
twitterLable=Label(root,image=twitter_logo,bg='white')
twitterLable.place(x=740,y=440)

signupLabel=Label(root,text='dont have an account?',font=('Open sans',9,'bold'),fg='firebrick1',bg="white")
signupLabel.place(x=590,y=500)

newaccountBotton=Button(root,text='create new one',font=('open sans',9,'bold underline'),
                   fg='blue',bg='white',activebackground='blue',
                   activeforeground='white',
                   cursor='hand2',bd=0,command=signup_page)
newaccountBotton.place(x=727,y=500)


root.mainloop()






