def comparar_numeros(numero_usuario,numero_consola):

    if numero_usuario < 0 or numero_usuario > 100:
        print("Error, recuerda que tu numero debe ser de 1 a 100\n--------------------")
    elif numero_usuario == numero_consola:
        print("Felicidades, encontraste el numero ganador")
        return 1
    elif numero_usuario > numero_consola:
        print("El numero ganador es menor que tu numero\n--------------------")
    elif numero_usuario < numero_consola:
        print("El numero ganador es mayor que tu numero\n--------------------")
