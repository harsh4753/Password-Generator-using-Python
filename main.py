from tkinter import *
from pwgenfunc import RandPass
#METHODS
def pwGenerator(size):
    data = RandPass(size)
    new_password = data[0]
    pw_strength = data[1]
    pw_color = data[2]
    PASSWORD.set(new_password);
    lbl_strength.configure(foreground="white", background=pw_color, text=pw_strength, font=('sans serif', 10, 'bold'), bd=10, height=1, width=10)
    gui.clipboard_clear()
    gui.clipboard_append(new_password)
    gui.update()
    gui.mainloop()

#WINDOW
gui = Tk()
gui.title("Password Generator")
width = 600
height = 262
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
gui.geometry("%dx%d+%d+%d" % (width, height, x, y))


#VARIABLES
PASSWORD = StringVar()
PW_SIZE = IntVar()
e1 = Entry(gui, text=PW_SIZE)
PW_SIZE.set(8) # sets the default value for PW size/length

#FRAME
Top = Frame(gui)
Top.pack(side=TOP)
Form = Frame(gui)
Form.pack(side=TOP)
Bot = Frame(gui)
Bot.pack(side=BOTTOM)
#LABEL WIDGET
lbl_title = Label(Top, font=('sans serif', 12, 'bold'), text="Select: Size >> Click: Generate Now", bd=1, relief=SOLID)
lbl_title.pack(fill=X)
lbl_password = Label(Form, font=('sans serif', 18), text="Password", bd=10)
lbl_password.grid(row=0, pady=10)
lbl_strength = Label(Form, font=('sans serif', 10, 'bold'), foreground="white", background="#6d0001", text="Weak", bd=10, height=1, width=10)
lbl_strength.grid(row=0, column=3, pady=10, padx=10)
lbl_pw_size = Label(Form, font=('sans serif', 18), text="Size", bd=10)
lbl_pw_size.grid(row=1, pady=10)
lbl_instructions = Label(Bot, width=width, font=('sans serif', 12, 'bold'), text="Result will be on clipboard.", bd=1, relief=SOLID)
lbl_instructions.pack(fill=X)
#ENTRY WIDGET
password = Entry(Form, textvariable=PASSWORD, font=(18), width=24)
password.grid(row=0, column=1)
pw_size = Scale(Form, from_=8, to=24, length=230,width=24,sliderlength=14, orient=HORIZONTAL, variable=PW_SIZE, font=(18))
pw_size.grid(row=1, column=1)

#BUTTON WIDGET
btn_generate = Button(Form, text="Generate Now", width=20, command=lambda: pwGenerator(PW_SIZE))
btn_generate.grid(row=2, column=1)

#INITIATOR

gui.mainloop()
