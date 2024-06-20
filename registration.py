from tkinter import *
from database import insert_data

def submit_form():
    name = name_value.get()
    branch = branch_value.get()
    gender = gender_value.get()
    contact = contact_value.get()
    email = email_value.get()
    address = address_value.get()
    
    # Call the insert_data function to insert the form data into the database
    insert_data(name, branch, gender, contact, email, address)
    print('Form submitted successfully')

root = Tk()
root.geometry("1980x1080")

# Create a frame to hold all the widgets and center it using pack
frame = Frame(root)
frame.pack(expand=True)

Label(frame, text="Registration Form", font="times 15 bold").grid(row=0, column=1, columnspan=2, pady=10)

name_user = Label(frame, text="Student Name:")
name_user.grid(row=1, column=0, padx=10, pady=5, sticky=E)
branch_name = Label(frame, text="Branch:")
branch_name.grid(row=2, column=0, padx=10, pady=5, sticky=E)
user_gender = Label(frame, text="Gender:")
user_gender.grid(row=3, column=0, padx=10, pady=5, sticky=E)
user_contact = Label(frame, text="Contact Number:")
user_contact.grid(row=4, column=0, padx=10, pady=5, sticky=E)
user_email = Label(frame, text="Email:")
user_email.grid(row=5, column=0, padx=10, pady=5, sticky=E)
user_address = Label(frame, text="Address:")
user_address.grid(row=6, column=0, padx=10, pady=5, sticky=E)

name_value = StringVar()
branch_value = StringVar()
gender_value = StringVar()
contact_value = StringVar()
email_value = StringVar()
address_value = StringVar()
rememberme_value = IntVar()

name_box = Entry(frame, textvariable=name_value)
name_box.grid(row=1, column=1, padx=10, pady=5)
branch_box = Entry(frame, textvariable=branch_value)
branch_box.grid(row=2, column=1, padx=10, pady=5)
gender_box = Entry(frame, textvariable=gender_value)
gender_box.grid(row=3, column=1, padx=10, pady=5)
contact_box = Entry(frame, textvariable=contact_value)
contact_box.grid(row=4, column=1, padx=10, pady=5)
email_box = Entry(frame, textvariable=email_value)
email_box.grid(row=5, column=1, padx=10, pady=5)
address_box = Entry(frame, textvariable=address_value)
address_box.grid(row=6, column=1, padx=10, pady=5)

rememberme = Checkbutton(frame, text="Remember me?", variable=rememberme_value)
rememberme.grid(row=7, column=1, pady=10)

Button(frame, text="Submit", command=submit_form).grid(row=8, column=1, pady=20)

root.mainloop()
