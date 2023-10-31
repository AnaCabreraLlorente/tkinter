import tkinter
from tkinter import SUNKEN
from PIL import ImageTk, Image
window = tkinter.Tk()
global index
index = 0
imagenes = ["2.png", "6.png", "9.png", "5.png", "1.png"]
boto_seguent = tkinter.Button(window, text="següent", command=lambda: seguent())
boto_seguent.grid(row= 2, column=1)
boto_anterior = tkinter.Button(window, text="anterior", command=lambda: anterior(),state=tkinter.DISABLED)
boto_anterior.grid(row= 2, column=2);
boto_sortir = tkinter.Button(window, text="sortir", command=lambda: sortir())
boto_sortir.grid(row= 2, column=3)
label_pag = tkinter.Label(window, text=str(index + 1) + "/" + str(len(imagenes)), bd= 3, relief=SUNKEN, anchor= "e")
label_pag.grid(row=6, column=3)


img = ImageTk.PhotoImage(Image.open(imagenes[index]))
label_imagen = tkinter.Label(window, image=img)
label_imagen.grid(row=1, columnspan=4)

def mostrarImatge():
    global index
    img = ImageTk.PhotoImage(Image.open(imagenes[index]))
    label_imagen.configure(image=img)
    label_imagen.image = img
    boto_anterior.config(state= tkinter.NORMAL if index > 0 else tkinter.DISABLED)
    label_pag = tkinter.Label(window, text=str(index + 1) + "/" + str(len(imagenes)), bd=3, relief=SUNKEN, anchor= "e")
    label_pag.grid(row=6, column=3)

def sortir():
    window.quit();

def anterior():
    global index
    if index > 0:
        index -= 1
        mostrarImatge()

def seguent():
    global index
    if index < len(imagenes) - 1:
        index += 1
        mostrarImatge()


window.mainloop()