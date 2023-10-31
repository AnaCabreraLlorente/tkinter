import os
import tkinter
import sqlite3

window= tkinter.Tk()
window.title("Gestion BD_basquet")
window.geometry("400x400")

nom = tkinter.Entry(window)
cognom = tkinter.Entry(window)
alçada = tkinter.Entry(window)
edat = tkinter.Entry(window)
nom.grid(row=1, column=2)
cognom.grid(row=2, column=2)
alçada.grid(row=3, column=2)
edat.grid(row=4, column=2)

def afegir_jugador():
    try:
        if not os.path.exists("./bd/"):
            os.mkdir("./bd/")
        var_BD = sqlite3.connect("./bd/" + "basquet.db")
        cursor_BD = var_BD.cursor()
        cursor_BD.execute("""CREATE TABLE IF NOT EXISTS jugadors(nom text, cognom text, alçada real, edat integer)""")
        cursor_BD.execute("INSERT INTO jugadors (nom, cognom, alçada, edat) VALUES (?, ?, ?, ?)",
                       (nom.get(), cognom.get(), alçada.get(), edat.get()))

        var_BD.commit()

        nom.delete(0, tkinter.END)
        cognom.delete(0, tkinter.END)
        alçada.delete(0, tkinter.END)
        edat.delete(0, tkinter.END)

        mensaje = messagebox.showinfo(window, "Jugador afegit")

    except sqlite3.Error as e:
        print("Error al conectar a la base de datos:", str(e))


def mostrar_dades():
    var_BD = sqlite3.connect("./bd/" + "basquet.db")
    cur_BD = var_BD.cursor()
    cur_BD.execute("SELECT *, oid FROM jugadors")
    var_dades = cur_BD.fetchall()
    for dades in var_dades:
        print(dades)
    var_BD.close()

label_nom = tkinter.Label(window, text="Nom: ")
label_cognom = tkinter.Label(window, text="Cognom: ")
label_alçada = tkinter.Label(window, text="Alçada: ")
label_edat = tkinter.Label(window, text="Edat: ")
label_nom.grid(row=1, column=1)
label_cognom.grid(row=2, column=1)
label_alçada.grid(row=3, column=1)
label_edat.grid(row=4, column=1)

boton = tkinter.Button(window, text="Afegir jugador", command=afegir_jugador)
boton.grid(row=5, columnspan=6, column=2)
boton = tkinter.Button(window, text="Mostrar jugadors", command=mostrar_dades)
boton.grid(row=6, columnspan=6, column=2)

window.mainloop()
