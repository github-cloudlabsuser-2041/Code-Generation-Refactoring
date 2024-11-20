#Calculadora simples em Python
#Autor: Matronc

#funcion calculadora simple con suma, resta, multiplicación y división

#funcion suma
def suma (x, y):
    return x + y

#funcion resta

def resta (x, y):
    return x - y

def multiplicacion (x, y):
    return x * y

def division (x, y):
    return x / y

print("Selecciona operación.")
print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.División")

while True: 
    #toma la entrada del usuario
    eleccion = input("Ingresa elección(1/2/3/4): ")

    #verifica si la elección es una de las 4 opciones
    if eleccion in ('1', '2', '3', '4'):
        num1 = float(input("Ingresa primer número: "))
        num2 = float(input("Ingresa segundo número: "))

        if eleccion == '1':
            print(num1, "+", num2, "=", suma(num1, num2))

        elif eleccion == '2':
            print(num1, "-", num2, "=", resta(num1, num2))

        elif eleccion == '3':
            print(num1, "*", num2, "=", multiplicacion(num1, num2))

        elif eleccion == '4':
            print(num1, "/", num2, "=", division(num1, num2))
        break
    else:
        print("Entrada inválida")



