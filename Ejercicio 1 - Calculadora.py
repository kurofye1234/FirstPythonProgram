##Ejercicio 1 - Calculadora 

print("Bienvenido a la calculadora") 

try:
    numero1 = int(input("Ingresa el primer numero: ")) 
    numero2= int(input("Ingresa el segundo numero:"))  

except ValueError: 
    print("Numero no valido")  

print("Indica que operacion quieres hacer?") 
opcion = input("+, -, *, /: ") 

if opcion == "+":
    resultado = numero1 + numero2 
    print(f"La suma de {numero1} y {numero2} es: {resultado}") 
elif opcion == "-":
    resultado = numero1 - numero2 
    print(f"La resta de {numero1} y {numero2} es: {resultado}") 
elif opcion == "*":
    resultado = numero1 * numero2 
    print(f"La multiplicacion de {numero1} y {numero2} es: {resultado}") 
elif opcion == "/":
    resultado = numero1 / numero2 
    print(f"La division de {numero1} y {numero2} es: {resultado}") 
else:
    print("Operacion no valida")  

