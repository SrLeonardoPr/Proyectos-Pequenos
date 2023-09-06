# Proyecto Calculadora en Tkinter
# Autor: Jose Leonardo Piñeres Ramirez

import tkinter as tk  #Importar la libreria

calculo = "" 
color_boton = "#D28C7B"
color_boton2 = "#EDCEC7"
color_boton3 = "#8D8D8D"


# ----- Funciones Necesarias ----
def add_a_calculo(symbol):
  global calculo
  
  calculo += str(symbol)
  
  opcion_A.delete(1.0, "end")
  opcion_A.insert(1.0, calculo)
  opcion_B.delete(1.0, "end")
  opcion_B.insert(1.0, calculo)



def operacion_calculo(symbol):
  global calculo
  calculo += str(symbol)
  oper.delete(1.0, "end")
  oper.insert(1.0, calculo)
  calculo = ""

def evaluar_calculo():
  global calculo
  try:
    resultado = str(eval(calculo))
    calculo = ""
    opcion_A.delete(1.0, "end")
    opcion_A.insert(1.0,resultado)
    opcion_B.delete(1.0, "end")
    opcion_B.insert(1.0,resultado)
  except:
    limpiar_terminal()
    opcion_A.insert(1.0, "Error")
    opcion_B.insert(1.0, "Error")


def operar():
    try:
        numero_binario1 = salida_binario.get("1.0", "end-1c")
        numero_binario2 = salida_binario2.get("1.0", "end-1c")
        operador = oper.get("1.0", "end-1c")
        
        numero_decimal1 = int(numero_binario1, 2)
        numero_decimal2 = int(numero_binario2, 2)
        
        if operador == "+":
            resultado_decimal = numero_decimal1 + numero_decimal2
        elif operador == "-":
            resultado_decimal = numero_decimal1 - numero_decimal2
        elif operador == "*":
            resultado_decimal = numero_decimal1 * numero_decimal2
        elif operador == "/":
            resultado_decimal = numero_decimal1 / numero_decimal2
        elif operador == "**":
            resultado_decimal = numero_decimal1 ** numero_decimal2
        else:
            limpiar_terminal()
            resultado_final.insert(1.0,"Operador no válido")
            return
        
        resultado_binario = bin(int(resultado_decimal))[2:]
        resultado_final.insert(1.0,resultado_binario)
    except ValueError:
        resultado_final.insert(1.0,"Error")

    
def limpiar_terminal():
  global calculo
  calculo = ""
  opcion_A.delete(1.0, "end")
  opcion_B.delete(1.0, "end")
  salida_binario.delete(1.0,"end")
  salida_binario2.delete(1.0,"end")
  oper.delete(1.0,"end")
  resultado_final.delete(1.0,"end")
  resultado_final2.delete(1.0,"end")

def select_option1(option):
    menu_label1.config(text=f" Elegiste: {option}",font=("San Francisco",10))
    if option == "Decimal":
        convertir_a_binario()
    elif option == "Binario":
        bin_a_bin()
    elif option == "Hexadecimal":
        hex_a_bin()
    elif option == "Octal":
        oct_a_bin()  
    

def select_option2(option2):
    menu_label2.config(text=f" Elegiste: {option2}",font=("San Francisco",10))
    if option2 == "Decimal":
        convertir_a_binario2()
    elif option2 == "Binario":
        bin_a_bin2()
    elif option2 == "Hexadecimal":
        hex_a_bin2()
    elif option2 == "Octal":
        oct_a_bin2()

def select_option3(option3):
    if option3 == "Decimal":
        bin_a_dec()
    elif option3 == "Binario":
        bin_a_bin3()
    elif option3 == "Hexadecimal":
        bin_a_hex()
    elif option3 == "Octal":
        bin_a_oct()

    
# ------ Interfaz grafica --------
ventana = root = tk.Tk()
ventana.title("Super Calculadora Taller V")
root.geometry("1200x720")

# ------ Definir sistema de conversiones ------
def convertir_a_binario():
    try:
        numero_decimal = int(opcion_A.get("1.0", "end-1c"))
        numero_binario = bin(numero_decimal)[2:]
        salida_binario.delete(1.0, "end")
        salida_binario.insert(1.0, numero_binario)
    except ValueError:
        salida_binario.delete(1.0, "end")
        salida_binario.insert(1.0, "Error")

def convertir_a_binario2():
    try:
        numero_decimal2 = int(opcion_B.get("1.0", "end-1c"))
        numero_binario2 = bin(numero_decimal2)[2:]
        salida_binario2.delete(1.0, "end")
        salida_binario2.insert(1.0, numero_binario2)
    except ValueError:
        salida_binario2.delete(1.0, "end")
        salida_binario2.insert(1.0, "Error")


def bin_a_bin():
    try:
        numero_decimal = int(opcion_A.get("1.0", "end-1c"))
        numero_binario = int(numero_decimal)
        salida_binario.delete(1.0, "end")
        salida_binario.insert(1.0, str(numero_binario))
    except ValueError:
        salida_binario.delete(1.0, "end")
        salida_binario.insert(1.0, "Error")

def bin_a_bin2():
    try:
        numero_decimal2 = int(opcion_B.get("1.0", "end-1c"))
        numero_binario2 = int(numero_decimal2)
        salida_binario2.delete(1.0, "end")
        salida_binario2.insert(1.0, str(numero_binario2))
    except ValueError:
        salida_binario2.delete(1.0, "end")
        salida_binario2.insert(1.0, "Error")


def hex_a_bin():
    try:
        numero_hex = opcion_A.get("1.0", "end-1c")
        numero_decimal = int(numero_hex, 16)
        numero_binario = bin(numero_decimal)[2:]
        salida_binario.delete(1.0, "end")
        salida_binario.insert(1.0, numero_binario)
    except ValueError:
        salida_binario.delete(1.0, "end")
        salida_binario.insert(1.0, "Error")

def hex_a_bin2():
    try:
        numero_hex2 = opcion_B.get("1.0", "end-1c")
        numero_decimal2 = int(numero_hex2, 16)
        numero_binario2 = bin(numero_decimal2)[2:]
        salida_binario2.delete(1.0, "end")
        salida_binario2.insert(1.0, numero_binario2)
    except ValueError:
        salida_binario2.delete(1.0, "end")
        salida_binario2.insert(1.0, "Error")


def oct_a_bin():
    try:
        numero_octal = opcion_A.get("1.0", "end-1c")
        numero_decimal = int(numero_octal, 8)
        numero_binario = bin(numero_decimal)[2:]
        salida_binario.delete(1.0, "end")
        salida_binario.insert(1.0, numero_binario)
    except ValueError:
        salida_binario.delete(1.0, "end")
        salida_binario.insert(1.0, "Error")
  
def oct_a_bin2():
    try:
        numero_octal2 = opcion_B.get("1.0", "end-1c")
        numero_decimal2 = int(numero_octal2, 8)
        numero_binario2 = bin(numero_decimal2)[2:]
        salida_binario2.delete(1.0, "end")
        salida_binario2.insert(1.0, numero_binario2)
    except ValueError:
        salida_binario2.delete(1.0, "end")
        salida_binario2.insert(1.0, "Error")


# ---------- CONVERSIONES RESULTADO FINAL ------------
def bin_a_dec():
    try:
        numero_binario3 = resultado_final.get("1.0", "end-1c")
        numero_decimal3 = int(numero_binario3, 2)
        resultado_final2.delete(1.0, "end")
        resultado_final2.insert(1.0, str(numero_decimal3))
    except ValueError:
        resultado_final2.delete(1.0, "end")
        resultado_final2.insert(1.0, "Error")

def bin_a_hex():
    try:
        numero_binario3 = resultado_final.get("1.0", "end-1c")
        numero_decimal3 = int(numero_binario3, 2)
        numero_hexadecimal = hex(numero_decimal3)[2:]
        resultado_final2.delete(1.0, "end")
        resultado_final2.insert(1.0, numero_hexadecimal)
    except ValueError:
        resultado_final2.delete(1.0, "end")
        resultado_final2.insert(1.0, "Error")

def bin_a_oct():
    try:
        numero_binario3 = resultado_final.get("1.0", "end-1c")
        numero_decimal3 = int(numero_binario3, 2)
        numero_octal = oct(numero_decimal3)[2:]
        resultado_final2.delete(1.0, "end")
        resultado_final2.insert(1.0, numero_octal)
    except ValueError:
        resultado_final2.delete(1.0, "end")
        resultado_final2.insert(1.0, "Error")

def bin_a_bin3():
    try:
        numero_binario3 = resultado_final.get("1.0", "end-1c")
        resultado_final2.delete(1.0, "end")
        resultado_final2.insert(1.0, numero_binario3)
    except ValueError:
        resultado_final2.delete(1.0, "end")
        resultado_final2.insert(1.0, "Error")




# ------ Interfaz Displays ---------
opcion_A_label = tk.Label(root, text="Primer numero:",font=("San Francisco",10))
opcion_A_label.grid(columnspan=5)
opcion_A = tk.Text(root, height=1, width =20, font= ("San Francisco",20),bd=5)
opcion_A.grid(columnspan=4)
opcion_B_label = tk.Label(root, text="Segundo Numero:",font=("San Francisco",10))
opcion_B_label.grid(columnspan=5)
opcion_B = tk.Text(root, height=1, width =20, font= ("San Francisco",20),bd=5)
opcion_B.grid(columnspan=4)

# ----- Menu operaciones ------
oper_label = tk.Label(root, text="Que operacion desea",font=("San Francisco",10))
oper_label.grid(row=5,column=4, columnspan=2)
oper = tk.Text(root, height=1, width =3, font= ("San Francisco",20),bd=5)
oper.grid(row=6,column=4, columnspan=2)

# ----- Interfaz Display Resultado ------

resultado_final_label1 = tk.Label(root, text="",font=("San Francisco",10))
resultado_final_label1.grid(row=13, columnspan=2)
resultado_final_label = tk.Label(root, text="El resultado final es = ",font=("San Francisco",10))
resultado_final_label.grid(row=14, columnspan=2)
resultado_final = tk.Text(root, height=1, width =20, font= ("San Francisco",20),insertwidth=4,bd=5)
resultado_final.grid(row=15, columnspan=4)

resultado_final_label2 = tk.Label(root, text="",font=("San Francisco",10))
resultado_final_label2.grid(row=16, columnspan=2)
resultado_final_label2 = tk.Label(root, text="Menu de conversion",font=("San Francisco",10))
resultado_final_label2.grid(row=16, columnspan=2)

resultado_final2 = tk.Text(root, height=1, width =20, font= ("San Francisco",20),insertwidth=4,bd=5)
resultado_final2.grid(row=18, columnspan=4)


# ---Botón de selección para alternar el modo---



#---------- Label Botones
texto_label1= tk.Label(root, text="---------Panel de botones------------ ",font=("San Francisco",10))
texto_label1.grid(row=4,columnspan=5)

#-------Botones Numeros -------
btn_1 = tk.Button(root,text="1",bg= color_boton,command=lambda:add_a_calculo(1),width=5,font= ("San Francisco",14))
btn_1.grid(row=5,column=0)
btn_2 = tk.Button(root,text="2",bg= color_boton,command=lambda:add_a_calculo(2),width=5,font= ("San Francisco",14))
btn_2.grid(row=5,column=1)
btn_3 = tk.Button(root,text="3",bg= color_boton,command=lambda:add_a_calculo(3),width=5,font= ("San Francisco",14))
btn_3.grid(row=5,column=2)
btn_4 = tk.Button(root,text="4",bg= color_boton,command=lambda:add_a_calculo(4),width=5,font= ("San Francisco",14))
btn_4.grid(row=5,column=3)
btn_5 = tk.Button(root,text="5",bg= color_boton,command=lambda:add_a_calculo(5),width=5,font= ("San Francisco",14))
btn_5.grid(row=6,column=0)
btn_6 = tk.Button(root, text="6",bg= color_boton, command=lambda: add_a_calculo(6), width=5, font=("San Francisco", 14))
btn_6.grid(row=6, column=1)
btn_7 = tk.Button(root, text="7",bg= color_boton, command=lambda: add_a_calculo(7), width=5, font=("San Francisco", 14))
btn_7.grid(row=6, column=2)
btn_8 = tk.Button(root, text="8",bg= color_boton, command=lambda: add_a_calculo(8), width=5, font=("San Francisco", 14))
btn_8.grid(row=6, column=3)
btn_9 = tk.Button(root, text="9",bg= color_boton, command=lambda: add_a_calculo(9), width=5, font=("San Francisco", 14))
btn_9.grid(row=7, column=0)
btn_0 = tk.Button(root, text="0",bg= color_boton, command=lambda: add_a_calculo(0), width=5, font=("San Francisco", 14))
btn_0.grid(row=7, column=1)

#------Botones letras-------
btn_a = tk.Button(root, text="A",bg= color_boton2, command=lambda: add_a_calculo("A"), width=5, font=("San Francisco", 14))
btn_a.grid(row=7, column=2)
btn_b = tk.Button(root, text="B",bg= color_boton2, command=lambda: add_a_calculo("B"), width=5, font=("San Francisco", 14))
btn_b.grid(row=7, column=3)
btn_c = tk.Button(root, text="C",bg= color_boton2, command=lambda: add_a_calculo("C"), width=5, font=("San Francisco", 14))
btn_c.grid(row=8, column=0)
btn_d = tk.Button(root, text="D",bg= color_boton2, command=lambda: add_a_calculo("D"), width=5, font=("San Francisco", 14))
btn_d.grid(row=8, column=1)
btn_e = tk.Button(root, text="E",bg= color_boton2, command=lambda: add_a_calculo("E"), width=5, font=("San Francisco", 14))
btn_e.grid(row=8, column=2)
btn_f = tk.Button(root, text="F",bg= color_boton2, command=lambda: add_a_calculo("F"), width=5, font=("San Francisco", 14))
btn_f.grid(row=8, column=3)

#-----Botones de operaciones------
btn_sum = tk.Button(root, text="+",bg= color_boton3, command=lambda: operacion_calculo("+"), width=5, font=("San Francisco", 14))
btn_sum.grid(row=9, column=0)
btn_rest = tk.Button(root, text="-",bg= color_boton3, command=lambda: operacion_calculo("-"), width=5, font=("San Francisco", 14))
btn_rest.grid(row=9, column=1)
btn_mult = tk.Button(root, text="*",bg= color_boton3, command=lambda: operacion_calculo("*"), width=5, font=("San Francisco", 14))
btn_mult.grid(row=9, column=2)
btn_div = tk.Button(root, text="/",bg= color_boton3, command=lambda: operacion_calculo("/"), width=5, font=("San Francisco", 14))
btn_div.grid(row=9, column=3)
btn_pote = tk.Button(root, text="^",bg= color_boton3, command=lambda: operacion_calculo("**"), width=5, font=("San Francisco", 14))
btn_pote.grid(row=10, column=0)
btn_result = tk.Button(root, text="=",bg= "#747474", command=operar, width=5, font=("San Francisco", 14))
btn_result.grid(row=10, column=3)

# -----Boton de Limpiar------
btn_Clear = tk.Button(root, text="Limpiar paneles",bg="#EEA93A",command= limpiar_terminal, width=15, font=("San Francisco", 12))
btn_Clear.grid(row=10, column=1,columnspan=2)

#------------------MENU-----------------------------
# Crear un Menubutton 1
menu_button1 = tk.Menubutton(ventana, text="Sistema numerico",font=("San Francisco",10),relief="raised")
menu_button1.grid(row=1, column=5)

# Crear un menú desplegable 1
option_menu1 = tk.Menu(menu_button1, tearoff=0)
menu_button1.configure(menu=option_menu1)

# Agregar opciones al menú 1
opciones1 = ["Decimal", "Binario", "Hexadecimal","Octal"]
for i, option in enumerate(opciones1):
    option_menu1.add_command(label=option, command=lambda opt=option: select_option1(opt))

menu_label1 = tk.Label(ventana, text="<---Selecciona una \n opción",font=("San Francisco",10))
menu_label1.grid(row=1, column=6)


# Crear un Menubutton 2
menu_button2 = tk.Menubutton(ventana, text="Sistema numerico",font=("San Francisco",10),relief="raised")
menu_button2.grid(row=3, column=5)

# Crear un menú desplegable 2
option_menu2 = tk.Menu(menu_button2, tearoff=0)
menu_button2.configure(menu=option_menu2)

# Agregar opciones al menú
opciones2 = ["Decimal", "Binario", "Hexadecimal","Octal"]
for i, option2 in enumerate(opciones2):
    option_menu2.add_command(label=option2, command=lambda opt=option2: select_option2(opt))

menu_label2 = tk.Label(ventana, text="<---Selecciona una \n opción",font=("San Francisco",10))
menu_label2.grid(row=3, column=6)


# Crear un Menubutton 3
menu_button3 = tk.Menubutton(ventana, text="Sistema Numerico",font=("San Francisco",10),relief="raised")
menu_button3.grid(row=16, column=4)

# Crear un menú desplegable 3
option_menu3 = tk.Menu(menu_button3, tearoff=0)
menu_button3.configure(menu=option_menu3)

# Agregar opciones al menú 3
opciones3 = ["Decimal", "Binario", "Hexadecimal","Octal"]
for i, option3 in enumerate(opciones3):
    option_menu3.add_command(label=option3, command=lambda opt=option3: select_option3(opt))
#-----------------------------------------------------------------

#Convertir a Bin

texto_label2 = tk.Label(ventana, text = "#1 en Bin",font=("San Francisco",10))
texto_label2.grid(row=11, columnspan=3)
salida_binario = tk.Text(root, height=1, width =15, font= ("San Francisco",20),bd=5)
salida_binario.grid(row=12, columnspan=3)

texto_label3 = tk.Label(ventana, text = "#2  en Bin",font=("San Francisco",10))
texto_label3.grid(row=11, column= 4, columnspan=2)
salida_binario2 = tk.Text(root, height=1, width =15, font= ("San Francisco",20),bd=5)
salida_binario2.grid(row=12, column= 4, columnspan=2)


root.mainloop()
