import random

rondas_totales = 5
opciones = ["piedra", "papel", "tijera"]

rondas_para_ganar = rondas_totales // 2 + 1

print("Bienvenido al juego")
print(f"Se juega a mejor de {rondas_totales} (gana quien llegue a {rondas_para_ganar}).")

puntos_usuario = 0
puntos_pc = 0
ronda = 1

def pedir_jugada():
    jugada = input("Elige: ").lower()
    while jugada not in opciones:
        print("Debe ser piedra, papel o tijera.")
        jugada = input("Elige: ").lower()
    return jugada

while ronda <= rondas_totales and puntos_usuario < rondas_para_ganar and puntos_pc < rondas_para_ganar:
    print(f"\nRonda {ronda}")
    jugada_usuario = pedir_jugada()
    jugada_pc = random.choice(opciones)
    print(f"La computadora eligió: {jugada_pc}")

    if jugada_usuario == jugada_pc:
        print("Empate.")
    elif (
        (jugada_usuario == "piedra" and jugada_pc == "tijera") or
        (jugada_usuario == "papel" and jugada_pc == "piedra") or
        (jugada_usuario == "tijera" and jugada_pc == "papel")
    ):
        print("Ganaste")
        puntos_usuario += 1
    else:
        print("Perdiste.")
        puntos_pc += 1

    print(f"Marcador: Usuario {puntos_usuario} - PC {puntos_pc}")
    ronda += 1

print("Resultado: ")
print(f"Tus puntos: {puntos_usuario} / Puntos de la pc: {puntos_pc}")

if puntos_usuario > puntos_pc:
    print("Ganaste el juego.")
elif puntos_usuario < puntos_pc:
    print("La computadora ganó el juego.")
else:
    print("Empate.")

