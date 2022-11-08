from tkinter import *
from tkinter import messagebox

FONT = "Arial"
FONT_SIZE = 12

# ---------------------------- PASSWORD GENERATOR ------------------------------- #





# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():

    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} "
                                                              f"\n Password: {password} \nIs it ok to save?")

        if is_ok:
            with open("passwords.txt", "a") as file:
                file.write(f"{website} | {email} | {password} \n")
                file.close()
                web_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website Label
website_lbl = Label(text="Website:", font=(FONT, FONT_SIZE))
website_lbl.grid(row=1, column=0)

# Website entry
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
web_entry.focus()

# Email Label
email_lbl = Label(text="Email/Username:", font=(FONT, FONT_SIZE))
email_lbl.grid(row=2, column=0)

# Email entry
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "mateusz3563@gmail.com")

# Password Label
password_lbl = Label(text="Password:", font=(FONT, FONT_SIZE))
password_lbl.grid(row=3, column=0)

# Password Entry
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, sticky="W")

# Password generation Button
generate_btn = Button(text="Generate Password")
generate_btn.grid(row=3, column=2)

# Add Button
add_btn = Button(text="Add", width=36, command=add_password)
add_btn.grid(row=4, column=1, columnspan=2, pady=5, sticky="EW")

window.mainloop()