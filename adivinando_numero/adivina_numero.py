import random
import adivinando_numero.comparacion_numeros as comparacion_numeros
def adivina_numero():
    victoria = 0 #inicializamos una variable que si su valor incrementa a 1 sera por que el usuario habra adivinado el numero
    intentos = 0 #inicializamos esta variable para contar los intentos que haga el usuario
    numero_intentos = int(input("¿CUANTOS INTENTOS DESEAS PARA ADIVINAR EL NUMERO?: "))#se le pregunta al usuario cuantos intentos quiere realizar

    numero_consola = random.randint(1,100)#le asignamos a la consola un numero aleatorio de 1 a 100
    print("La consola ha elegido el numero")
    while True: #iniciamos un bucle para que ser repita hasta que el usuario gane o pierda por numero de intentos
        numero_usuario = int(input("ingresa un numero del 1 al 100: "))#le indicamos al usuario que escoja un numero del 1 al 100

        victoria = comparacion_numeros.comparar_numeros(numero_usuario,numero_consola)
        """en la variable victoria guardamos el valor que retorne la funcion, el cual vale lo mismo que cuando se inicializa en la liea 4
        a menos que el usuario gane"""

        intentos += 1 #esta variable incrementara cada vez que el usuario haga un intento

        if victoria == 1:#si el usuario gana terminara el bucle
            break
        elif intentos == numero_intentos:#si el usuario realiza todos los intentos y pierde, termina el juego y sale del bucle
            print(f"Game over, se acabaron tus intentos\nEL NUMERO GANADOR ES: {numero_consola}")
            break