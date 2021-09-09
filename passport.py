from tkinter import * 
from tkinter import Menu

root = Tk()
# Adjust size
root.geometry("1600x800+0+0")
root.title("PASSPORT AUTOMATION SYSTEM") 
Label(root, text="",font=('arial',40)).pack()
# Add image file
bg = PhotoImage(file = "capture.png")

# Create Canvas
canvas1 = Canvas( root, width = 400,height = 400)

canvas1.pack(fill = "both", expand = True)

# Display image
canvas1.create_image( 0, 0, image = bg,anchor = "nw")

def _quit():  
   win.quit()  
   win.destroy()  
   exit()
def tik():
    import colortkinter
#Create Menu Bar  
menuBar=Menu(root)  
root.config(menu=menuBar)  
#File Menu  
fileMenu= Menu(menuBar, tearoff=0)  
fileMenu.add_command(label="New")  
fileMenu.add_separator()  
fileMenu.add_command(label="Exit", command=_quit)  
menuBar.add_cascade(label="File", menu=fileMenu)  
#Help Menu  
helpMenu= Menu(menuBar, tearoff=0)  
helpMenu.add_command(label="About")  
menuBar.add_cascade(label="Help", menu=helpMenu)
#ks menu
ksMenu= Menu(menuBar, tearoff=0)  
ksMenu.add_command(label="ok", command=tik)
ksMenu.add_separator()
ksMenu.add_command(label="ko")
ksMenu.add_separator()
menuBar.add_cascade(label="Kaushal", menu=ksMenu)
#Calling Main()  

root.mainloop()
