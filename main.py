from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- CONSTANTS ------------------------------- #

BLACK = "#000000"
BLUE = "#2192FF"
FONT_UI = "montserrat"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.insert(0,password)
    
    pyperclip.copy(password)

# ---------------------------- SEARCH ------------------------------- #
def find_password():
    print("pressed")
    website_name = website_entry.get()
    try:
        with open("passwords.json","r") as passw_file:
            passw_data = json.load(passw_file)
    except FileNotFoundError :
        messagebox.showinfo(title="Error",message="No data file found")
    else:            
        if website_name in passw_data:
            req_email = passw_data[website_name]["email"]
            req_passw = passw_data[website_name]["password"]
            messagebox.showinfo(title=website_name,message=f"Email: {req_email}\nPassword: {req_passw}")   
        else:     
            messagebox.showinfo(title="Error",message=f"No data found for {website_name}")      

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    we = website_entry.get() 
    ee = email_entry.get()
    pe = password_entry.get()
    new_data = {we : {
        "email" : ee,
        "password": pe
    }}
    
    if len(we) == 0 or len(pe) == 0:
        messagebox.showerror(title="Error",message="Please don't leave any empty fields.")        
    else:
        is_ok = messagebox.askokcancel(title=we,message=f"There are the details you entered: \n Email: {ee} \n Password: {pe} \n Click ok to confirm:")
        try:
            if is_ok:
                with open("passwords.json",'r') as file :
                    data = json.load(file) 
                    data.update(new_data) 
                
                with open("passwords.json",'w') as file :
                    json.dump(data,file,indent=4) 
                website_entry.delete(0,END)
                password_entry.delete(0,END)    
        except FileNotFoundError:
                with open("passwords.json",'w') as file :
                    json.dump(new_data,file,indent=4) 
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)    
            
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=400,height=400)
window.config(padx=50,pady=50,bg=BLACK)

canvas = Canvas(width=200,height=200,bg=BLACK,highlightthickness=0)
password_img = PhotoImage(file="logo.png")
canvas.create_image(90,90,image = password_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website",font=(FONT_UI,20),bg=BLACK,fg=BLUE)
website_label.grid(column=0,row=1)

website_entry = Entry(width=20,font=(FONT_UI,18))
website_entry.grid(column=1,row=1)
website_entry.focus()

search_btn = Button(text="Search",font=(FONT_UI,14),fg="white",bg=BLACK,width=16,command=find_password)
search_btn.grid(column=2,row=1)

email_label = Label(text="Email/Username:",font=(FONT_UI,20),bg=BLACK,fg=BLUE)
email_label.grid(column=0,row=2)

email_entry = Entry(width=35,font=(FONT_UI,18))
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"example@gmail.com")

password_label = Label(text="Password:",font=(FONT_UI,20),bg=BLACK,fg=BLUE)
password_label.grid(column=0,row=3)

password_entry = Entry(width=20,font=(FONT_UI,18))
password_entry.grid(column=1,row=3)

gen_password_btn = Button(text="Generate Password",font=(FONT_UI,14),fg="white",bg=BLACK,command=generate_password,width=16)
gen_password_btn.grid(column=2,row=3)

add_btn = Button(text="Add",font=(FONT_UI,12),fg="white",bg=BLACK,width=60,command=save)
add_btn.grid(column=0,row=4,columnspan=3)

window.mainloop()
