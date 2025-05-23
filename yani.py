print("Buenas")
# Ejemplo sencillo de Python: Saludar al usuario

def saludar():
    nombre = input("Introduce tu nombre: ")
    print("¡Hola, " + nombre + "! Bienvenido a Python.")

if __name__ == "__main__":
    saludar()

print ("B")

import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("¡Bienvenido al juego 'Adivina el Número'!")
    print("He seleccionado un número entre 1 y 100. ¿Puedes adivinar cuál es?")
    
    while True:
        try:
            intento = int(input("Introduce un número: "))
            intentos += 1
            
            if intento < numero_secreto:
                print("El número es mayor. Intenta de nuevo.")
            elif intento > numero_secreto:
                print("El número es menor. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    adivina_el_numero()

print ("C")