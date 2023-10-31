import tkinter
from tkinter import messagebox
window = tkinter.Tk()
window.title("Ventana principal")
text = "Has clickat: "


def mostrar_ventana_emergente():
    opcion1 = messagebox.askquestion("Ventana emergente", "Pulsa si o no")
    opcion2 = messagebox.askyesno("Ventana emergente", "¿Desea continuar?")
    opcion3 = messagebox.askquestion("Ventana emergente", "Hola")
    respuesta1 = tkinter.Label(window, text=text + str(conversion(opcion1)))
    respuesta2 = tkinter.Label(window, text=text + str(conversion(opcion2)))
    respuesta3 = tkinter.Label(window, text=text + str(conversion(opcion3)))
    respuesta1.pack()
    respuesta2.pack()
    respuesta3.pack()


boton = tkinter.Button(window, text="Mostrar ventana", command=mostrar_ventana_emergente)
boton.pack()

def conversion(opcion):
    if opcion == True or opcion == "yes":
        return "si"
    else: return "no"



window.mainloop()