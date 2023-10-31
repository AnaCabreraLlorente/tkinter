import os
from tkinter import filedialog as quelcom
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Seleccionar y Mostrar Imagen")
window.geometry("400x400")

def abrir_imagen():
    archivo = quelcom.askopenfilename(initialdir=os.getcwd(), title="Selecciona una imagen", filetypes=(("Todos los archivos", "*.*"), ("Imágenes JPG", "*.jpg")))

    if archivo:
        ventana_imagen = Toplevel(window)
        ventana_imagen.title("Imagen Seleccionada")

        etiqueta_path = Label(ventana_imagen, text="Path de la imagen:" + "\n" + archivo)
        etiqueta_path.pack()

        imagen = Image.open(archivo)
        imagen_tk = ImageTk.PhotoImage(imagen)
        label_imagen = Label(ventana_imagen, image=imagen_tk)
        label_imagen.image = imagen_tk
        label_imagen.pack()

        def guardar_imagen():
            archivo_guardar = quelcom.asksaveasfilename(defaultextension=".jpg", filetypes=(("Imágenes JPG", "*.jpg"), ("Todos los archivos", "*.*")))
            if archivo_guardar:
                imagen.save(archivo_guardar)

        boton_guardar = Button(ventana_imagen, text="Guardar Imagen", command=guardar_imagen)
        boton_guardar.pack()

boton_abrir_imagen = Button(window, text="Abrir Imagen", command=abrir_imagen)
boton_abrir_imagen.pack()
window.mainloop()
