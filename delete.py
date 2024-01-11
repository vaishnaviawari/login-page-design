import signin
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import messagebox
from PIL import ImageTk
import signup
import tk
import pymysql
def delete_account():

    window1 = Tk()

    window1.title('Delete Account')
    bgPic = ImageTk.PhotoImage(file='bg2.jpg')
    bgLable = Label(window1, image=bgPic)
    bgLable.grid()

    window1.mainloop()













#
#
# import tkinter as tk
#
# def delete_account():
#     window1 = tk.Toplevel()  # Create a new window (Toplevel) for delete account functionality
#     window1.title('Delete Account')  # Set the title of the new window
#
#     # Add your delete account GUI elements and logic inside this window
#     # For example:
#     label = tk.Label(window1, text="Are you sure you want to delete your account?")
#     label.pack()
#
#     confirm_button = tk.Button(window1, text="Confirm Delete", command=confirm_delete)
#     confirm_button.pack()
#
# def confirm_delete():
#     # Your account deletion logic here
#     pass
#
# root = tk.Tk()  # Create the root window
#
# deleteButton = tk.Button(root, text='Delete Account.', font=('Microsoft yahei UI Light', 9, 'bold'),
#                          fg='firebrick1', bg='white', activebackground='white',
#                          activeforeground='firebrick1',
#                          cursor='hand2', bd=0, command=delete_account)
# deleteButton.place(x=715, y=315)
#
#
#
# root.mainloop()  # Start the GUI event loop



