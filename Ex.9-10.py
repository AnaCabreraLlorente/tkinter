import tkinter
window = tkinter.Tk()
quadre = tkinter.Entry(window, width=22)
quadre.grid(rowspan=1, columnspan=6)
resultado = 0
def delete():
    quadre.delete(0, tkinter.END)


def calcular():
    text = quadre.get()
    if "+" in text:
        num = text.split("+")
        resultado = int(num[0]) + int(num[1])
        delete()
        quadre.insert(0, resultado)
    elif "-" in text:
        num = text.split("-")
        resultado = int(num[0]) - int(num[1])
        delete()
        quadre.insert(0, resultado)
    elif "*" in text:
        num = text.split("*")
        resultado = int(num[0]) * int(num[1])
        delete()
        quadre.insert(0, resultado)
    elif "/" in text:
        num = text.split("/")
        resultado = int(num[0]) / int(num[1])
        delete()
        quadre.insert(0, resultado)


button0 = tkinter.Button(window, text="0", bg="grey", width=5, height=2, command=lambda: click_boto(0))
button0.grid(row= 6, column=2)
button1 = tkinter.Button(window, text="1", bg="grey", width=5, height=2, command=lambda: click_boto(1))
button1.grid(row=5, column=1)
button2 = tkinter.Button(window, text="2", bg="grey", width=5, height=2, command=lambda: click_boto(2))
button2.grid(row=5, column= 2)
button3 = tkinter.Button(window, text="3", bg="grey", width=5, height=2, command=lambda: click_boto(3))
button3.grid(row=5, column=3)
button4 = tkinter.Button(window, text="4", bg="grey", width=5, height=2, command=lambda: click_boto(4))
button4.grid(row=4, column=1)
button5 = tkinter.Button(window, text="5", bg="grey", width=5, height=2, command=lambda: click_boto(5))
button5.grid(row=4, column=2)
button6 = tkinter.Button(window, text="6", bg="grey", width=5, height=2, command=lambda: click_boto(6))
button6.grid(row=4, column=3)
button7 = tkinter.Button(window, text="7", bg="grey", width=5, height=2, command=lambda: click_boto(7))
button7.grid(row=3, column=1)
button8 = tkinter.Button(window, text="8", bg="grey", width=5, height=2, command=lambda: click_boto(8))
button8.grid(row=3, column=2)
button9 = tkinter.Button(window, text="9", bg="grey", width=5, height=2, command=lambda: click_boto(9))
button9.grid(row=3, column=3)
button_delete = tkinter.Button(window, text= "C", bg="grey", width=5, height=2, command= delete)
button_delete.grid(row= 6, column=1)
button_sum = tkinter.Button(window, text= "+", bg="grey", width=5, height=2, command=lambda: click_boto("+"))
button_sum.grid(row = 7, column=1)
button_resta = tkinter.Button(window, text="-", bg="grey", width=5, height=2, command=lambda: click_boto("-"))
button_resta.grid(row=7, column=2)
button_igual = tkinter.Button(window, text= "=", bg="grey", width=18, height=2, command=calcular)
button_igual.grid(rows=8, columnspan=4)
button_multiplicar = tkinter.Button(window, text= "*", bg="grey", width=5, height=2, command=lambda: click_boto("*"))
button_multiplicar.grid(row=7, column=3)
button_dividir = tkinter.Button(window, text= "/", bg="grey", width=5, height=2, command=lambda: click_boto("/"))
button_dividir.grid(row=6, column=3)



def click_boto(p):
    quadre.insert(tkinter.END, p)




window.mainloop()