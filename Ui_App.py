# =========== Librarys =========
from tkinter import *
import Backend_App as Commands
# =========== Setting ==========
root = Tk()
root.title("Get Screen Shot")
root.resizable(width=False,height=False)
# ============= Widget ==================
btn_screen_shot = Button(root,text="Get Screen Shot",command=Commands.get_screen_shot)
btn_screen_shot.grid(row=0,column=0)
# ============= Loop ==============
root.mainloop()
# =E=N=D======= Loop ==============
