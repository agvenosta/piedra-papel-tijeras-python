nombre1 = input ("Como se llama el jugador 1?: ")
nombre2 = input ("Como se llama el jugador 2?: ")

jugador1 = input("Hola Jugador 1! Que eliges? Piedra, papel o tijeras?: ")
jugador2 = input("Hola Jugador 2! Que eliges? Piedra, papel o tijeras?: ")

condition1 = jugador1 == "Piedra" and jugador2 == "Tijeras"
condition2 = jugador1 == "Papel" and jugador2 == "Piedra"
condition3 = jugador1 == "Tijeras" and jugador2 == "Papel"

if jugador1 == jugador2:
    print("Ha sido un empate!")
elif condition1 or condition2 or condition3: 
    print("Ha ganado: ", nombre1)
else:
    print("Ha ganado: ", nombre2)