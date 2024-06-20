#GUI (graphical user interface)

from tkinter import *
root = Tk()
root.geometry("1980x1080")

def submit_form():
    print('form submitted successfuly')



Label(root, text="Registration Form", font="times 15 bold").grid(row=0, column=3)

name_user = Label(root, text=" Student Name: " )
name_user.grid(row=1,column=3)
branch_name= Label(root, text=" Branch: " )
branch_name.grid(row=2,column=3)
user_gender= Label(root, text=" Gender: " )
user_gender.grid(row=3,column=3)
user_contact= Label(root, text=" Contact Number: " ) 
user_contact.grid(row=4,column=3)
user_email= Label(root, text="Email : " )
user_email.grid(row=5,column=3)
user_address= Label(root, text=" Address: " )
user_address.grid(row=6,column=3)


name_value= StringVar
branch_value= StringVar
gender_value= StringVar
contact_value= StringVar
email_value= StringVar
address_value= StringVar
rememberme_value=IntVar


name_box= Entry(root, textvariable=name_value).grid(row=1, column=4)
branch_box= Entry(root, textvariable=branch_value).grid(row=2, column=4)
gender_box= Entry(root, textvariable=gender_value).grid(row=3, column=4)
contact_box= Entry(root, textvariable=contact_value).grid(row=4, column=4)
email_box= Entry(root, textvariable=email_value).grid(row=5, column=4)
address_box= Entry(root, textvariable=address_value).grid(row=6, column=4)


rememberme =Checkbutton(text="Remember me?",variable=rememberme_value).grid(row=8, column=5)

Button(text="Submit",command=submit_form()).grid(row=10, column=5)

root.mainloop()