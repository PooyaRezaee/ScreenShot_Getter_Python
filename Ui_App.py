# =========== Librarys =========
from tkinter import *
import Backend_App as Commands
# =========== Setting ==========
root = Tk()
root.title("Get Screen Shot")
root.resizable(width=False,height=False)
root.configure(bg="white")
# ============= Widget ==================
text_enter_format = Label(root,text="Enter Your Format : ",bg="white")
text_enter_format.grid(row=0,column=0)

input_format = Entry(root)
input_format.grid(row=0,column=1)

btn_screen_shot = Button(root,text="Get Screen Shot",bg="#e8ffea",command=lambda : Commands.get_screen_shot(format_picture=input_format.get()))
btn_screen_shot.grid(row=1,column=0,columnspan=2)
# ============= Loop ==============
root.mainloop()
# =E=N=D======= Loop ==============

