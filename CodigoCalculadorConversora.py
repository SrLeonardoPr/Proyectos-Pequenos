#CALCULADORA DE SISTEMAS NUMERICOS CON CONVER5IONES Y CON LAS OPERACIONES ARITMETICAS
#Codigo desarrollado por Jose Leonardo Pineres


# Funcion para convertir de decimal a binario
def decimal_a_binario(numero):
  return bin(numero)[2:]


# Funcion para convertir de decimal a octal
def decimal_a_octal(numero):
  return oct(numero)[2:]


# Funcion para convertir de decimal a hexadecimal
def decimal_a_hexadecimal(numero):
  return hex(numero)[2:]


# Funcion para convertir entre sistemas numericos
def convertir_sistemas_numericos(numero, sistema_origen, sistema_destino):
  # Convertir a decimal primero
  if sistema_origen == "binario":
    decimal = int(numero, 2)
  elif sistema_origen == "octal":
    decimal = int(numero, 8)
  elif sistema_origen == "hexadecimal":
    decimal = int(numero, 16)
  else:
    decimal = int(numero)

  # Convertir al sistema destino
  if sistema_destino == "binario":
    return decimal_a_binario(decimal)
  elif sistema_destino == "octal":
    return decimal_a_octal(decimal)
  elif sistema_destino == "hexadecimal":
    return decimal_a_hexadecimal(decimal)
  else:
    return decimal


# Funcion para realizar operaciones aritmeticas en sistema binario
def operar_binario(num1, num2, operador):
  # Convertir numeros a decimal
  decimal_num1 = int(num1, 2)
  decimal_num2 = int(num2, 2)

  # Realizar la operacion aritmetica correspondiente
  if operador == "+":
    resultado_decimal = decimal_num1 + decimal_num2
  elif operador == "-":
    resultado_decimal = decimal_num1 - decimal_num2
  elif operador == "*":
    resultado_decimal = decimal_num1 * decimal_num2
  elif operador == "/":
    if decimal_num2 == 0:
      return "Error: no se puede dividir entre cero"
    resultado_decimal = decimal_num1 / decimal_num2
  else:
    return "Operador no valido"

  # Convertir resultado a binario
  resultado_binario = decimal_a_binario(resultado_decimal)
  return resultado_binario


# Funcion para realizar la suma
def sumar(num1, num2):
  return num1 + num2


# Funcion para realizar la resta
def restar(num1, num2):
  return num1 - num2


# Funcion para realizar la multiplicacion
def multiplicar(num1, num2):
  return num1 * num2


# Funcion para realizar la division
def dividir(num1, num2):
  return num1 / num2


# Funcion para realizar la potencia
def potencia(num1, num2):
  return num1**num2


# Funcion para realizar la raiz cuadrada
def raiz_cuadrada(num):
  return num**0.5


# Menu principal de la calculadora
def menu():
  print(
    "\nBienvenido a la calculadora\n \nEste codigo fue desarrollado por estudiantes de la Universidad Nacional de Colombia sede Manizales, para la materia Taller V de Ing Fisica\n"
  )
  print("1. Sumar")
  print("2. Restar")
  print("3. Multiplicar")
  print("4. Dividir")
  print("5. Potencia")
  print("6. Raiz cuadrada")
  print("7. Convertir entre sistemas numericos")
  print("8. Salir")
  print("9. Operar en binarios\n")


# Funcion principal del programa
def main():
  while True:
    menu()
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
      num1 = float(input("Ingrese el primer numero: "))
      num2 = float(input("Ingrese el segundo numero: "))
      resultado = sumar(num1, num2)
      print("El resultado es:", resultado)

    elif opcion == "2":
      num1 = float(input("Ingrese el primer numero: "))
      num2 = float(input("Ingrese el segundo numero: "))
      resultado = restar(num1, num2)
      print("El resultado es:", resultado)

    elif opcion == "3":
      num1 = float(input("Ingrese el primer numero: "))
      num2 = float(input("Ingrese el segundo numero: "))
      resultado = multiplicar(num1, num2)
      print("El resultado es:", resultado)

    elif opcion == "4":
      num1 = float(input("Ingrese el primer numero: "))
      num2 = float(input("Ingrese el segundo numero: "))
      if num2 == 0:
        print("Error: no se puede dividir entre cero")
      else:
        resultado = dividir(num1, num2)
        print("El resultado es:", resultado)

    elif opcion == "5":
      base = float(input("Ingrese la base: "))
      exponente = float(input("Ingrese el exponente: "))
      resultado = potencia(base, exponente)
      print("El resultado es:", resultado)

    elif opcion == "6":
      num = float(input("Ingrese el numero: "))
      if num < 0:
        print(
          "Error: no se puede calcular la raiz cuadrada de un numero negativo")
      else:
        resultado = raiz_cuadrada(num)
        print("El resultado es:", resultado)

    elif opcion == "7":
      numero = input("Ingrese el numero a convertir: ")
      sistema_origen = input(
        "Ingrese el sistema numerico origen (binario, octal, hexadecimal o decimal): "
      )
      sistema_destino = input(
        "Ingrese el sistema numerico destino (binario, octal, hexadecimal o decimal): "
      )
      resultado = convertir_sistemas_numericos(numero, sistema_origen,
                                               sistema_destino)
      if resultado == "Error: sistemas numericos no validos":
        print(resultado)
      else:
        print("El resultado es:", resultado)

    elif opcion == "8":
      print("Gracias por usar la calculadora")
      break

    elif opcion == "9":
      num1 = input("Ingrese el primer numero binario: ")
      num2 = input("Ingrese el segundo numero binario: ")
      operador = input("Ingrese el operador (+, -, *, /): ")
      resultado = operar_binario(num1, num2, operador)
      print("El resultado es:", resultado)

    else:
      print("Opcion no valida")


if __name__ == "__main__":
  main()
