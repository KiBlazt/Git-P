
print("hola como estas")
import os

laberinto = [
    ["#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", "#"],
    ["#", " ", "#", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#"],
    ["#", " ", " ", "#", " ", "#"],
    ["#", "#", "#", "#", "F", "#"]
]

pos_x, pos_y = 1, 1  # Posición inicial del jugador

def mostrar_laberinto():
    os.system("cls" if os.name == "nt" else "clear")
    for y in range(len(laberinto)):
        for x in range(len(laberinto[0])):
            if x == pos_x and y == pos_y:
                print("P", end=" ")
            else:
                print(laberinto[y][x], end=" ")
        print()

def mover(dx, dy):
    global pos_x, pos_y
    nuevo_x = pos_x + dx
    nuevo_y = pos_y + dy
    if laberinto[nuevo_y][nuevo_x] != "#":
        pos_x, pos_y = nuevo_x, nuevo_y

while True:
    mostrar_laberinto()
    if laberinto[pos_y][pos_x] == "F":
        print("¡Has llegado al final del laberinto!")
        break
    movimiento = input("Movimiento (WASD): ").lower()
    if movimiento == "w":
        mover(0, -1)
    elif movimiento == "s":
        mover(0, 1)
    elif movimiento == "a":
        mover(-1, 0)
    elif movimiento == "d":
        mover(1, 0)


        # Ejemplo 1: Laberinto más grande
        laberinto_grande = [
            ["#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", " ", " ", " ", "#", " ", " ", "#"],
            ["#", " ", "#", " ", "#", " ", "#", "#"],
            ["#", " ", "#", " ", " ", " ", " ", "#"],
            ["#", " ", "#", "#", "#", "#", " ", "#"],
            ["#", " ", " ", " ", " ", "#", " ", "#"],
            ["#", "#", "#", "#", " ", "#", "F", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#"]
        ]

        # Ejemplo 2: Laberinto con múltiples finales
        laberinto_multifinal = [
            ["#", "#", "#", "#", "#", "#"],
            ["#", " ", " ", " ", "F", "#"],
            ["#", " ", "#", " ", "#", "#"],
            ["#", " ", "#", " ", " ", "#"],
            ["#", "F", " ", "#", " ", "#"],
            ["#", "#", "#", "#", "#", "#"]
        ]

        # Ejemplo 3: Laberinto con obstáculos adicionales
        laberinto_obstaculos = [
            ["#", "#", "#", "#", "#", "#"],
            ["#", " ", " ", " ", "#", "#"],
            ["#", " ", "#", "O", " ", "#"],
            ["#", " ", "#", "#", " ", "#"],
            ["#", " ", "O", "#", "F", "#"],
            ["#", "#", "#", "#", "#", "#"]
        ]

        # Puedes cambiar el laberinto actual asignando uno de los ejemplos
        laberinto = laberinto_grande  # Cambia a laberinto_multifinal o laberinto_obstaculos si lo deseas


    for i in range(5):
        print("prinst", i + 1)