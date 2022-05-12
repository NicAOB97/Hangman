## Este codigo permite realizar el juego del ahorcado. Proporciona un interfaz que puede ser empleado por dos o mas jugadores para jugar al juego. 

# El primer jugador debera introducir una palabra al azar
palabra = input("Dime una palabra! " )

# Aqui se cuenta el numero de letras de la palabra y se crea un 'tablero' en blanco 
# luego se imprime una fila de tantas lineas como letras haya 
conteo = 0
for letras in palabra: 
    conteo += 1

p_camuflada = ["_"] * conteo
print(' '.join(map(str,p_camuflada)))

# El/la segund@ jugador@ tendra 6 vidas 
numero_vidas = 6

# Ahora, se le permite al segund@ jugador@ introducir letras de uno en uno
# si está en la palabra, se rellenaran todas las incidencias de esa letra en el tablero, gana si adivina la palabra
# si no, se le restara una vida, pierde si pierde las 6
while numero_vidas > 0:
    if "_" in (p_camuflada):
        letra_usuario = input("Dame una letra ")
        try :
            palabra.index(letra_usuario)
        except ValueError as e: 
            numero_vidas -= 1
            print("Perdiste una vida, te quedan", numero_vidas, "vidas")
        else: 
            for i in range(len(palabra)):
                if letra_usuario == palabra[i] :
                    p_camuflada[i] = letra_usuario
            print(' '.join(map(str,p_camuflada)))
    else:
        print("Adivinaste la palabra:", palabra, ", ganaste!" )
        break
else: 
    print("Has perdido! Fin del juego")