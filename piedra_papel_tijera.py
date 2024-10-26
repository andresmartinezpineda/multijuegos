import random
import escoger
import ganador

def piedra_papel_tijera():
    #inicializamos 2 variables qur usaremos mas adelante
    iteraciones = 0
    victoria = 0

    print("¡¡¡¡¡¡EL JUEGO TERMINARA SOLO SI GANAS!!!!!!") #le avisamos al jugador que el juego solo termina si gana
    print(" \n ----------------------------- \n  ")

    while victoria != 1:

        if iteraciones > 0: #si el usuario pierde o empata se imprime el siguiente mensaje
            print(" \n-------DEBES GANAR INTENTA DE NUEVO-------\n ")

        opcion = int(input("Elige una de las siguientes opciones: \n (1)piedra \n (2)papel \n (3) tijera \n"))
        #le pedimos al usuario que ingrese la opcion con un numero  y la guardamos en la variable (opcion)
        if opcion < 0 or opcion > 4:
            print("ERROR TU NUMERO DEBE SER DE 1 A 5 \n ")

        opcion_usuario = escoger.escoger_opcion(opcion)
        """creamos una funcion para cambiar la opcion de numero a letras, ya sea piedra papel o tijera y con un valor de retorno
        en este caso el valor de retorno se guardara en (opcion_usuario)"""

        opcion = random.randint(1,3)#le asignamos otro valor a la variable opcion, y el valor sera un numero aleatorio de 1 a 3

        opcion_consola = escoger.escoger_opcion(opcion)
        """llamamos de nuevo a la funcion pasando como parametro la variable reciclada (opcion) y se almacenara el valor de retorno en la 
        variable (opcion_consola)"""

        victoria = ganador.ganador(opcion_usuario,opcion_consola)
        """llamo a la funcion (ganador) y si el usuario pierde retornara 0 y seguira en el bucle, pero si el usuario gana retornara 1
        y el usuario podra terminar el bucle"""

        iteraciones += 1 #cuenta los intentos que hace el usuario para ganar, se utiliza en la linea 13 para informarle al usuario que debe ganar

    print(f"ganaste con {iteraciones} intentos")
