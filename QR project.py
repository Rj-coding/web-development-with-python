from tkinter import *
from tkinter import messagebox 
import pyqrcode
tk=Tk()
tk.title("QRgenerator")
tk.config(bg="#b3ccff")

def generate_QR():
    if len(user_input.get()) !=0 :
        global qr,img
        qr=pyqrcode.create(user_input.get())
        img=BitmapImage(data=qr.xbm(scale=10))
    else:
        messagebox.showwarning('warning',"fields are required!")
    try:
        display_code()
    except:
        pass
    
def display_code():
    img_lbl.config(image=img)
    output.config(text="Qr code : "+user_input.get())
lbl=Label(tk,text="enter text or URL",bg="#bbff99",padx=30,pady=10,font=("Courier",10))
lbl.pack()
 
user_input=StringVar()
entry=Entry(tk,textvariable=user_input,width=100,font=("ariel",10))
entry.pack(padx=20,pady=30)

button=Button(tk,text="generate qr",width=20,command=generate_QR,font=("ariel",10))
button.pack(padx=10,pady=1)
img_lbl=Label(tk,bg="#e6e6e6")
img_lbl.pack()

output=Label(tk,text="",bg="#F25252")
output.pack()
tk.mainloop()