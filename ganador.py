def ganador(opcion_usuario,opcion_consola):

    

    #EMPATE
    if opcion_consola == opcion_usuario:
        print(f" tu = {opcion_usuario}      VS    consola = {opcion_consola} \n EMPATE")
        """si la consola elige lo mismo que el usuario sera empate"""

    # OPCIONES DE GANAR
    elif opcion_usuario == "piedra"  and opcion_consola == "tijera": #USUARIO = PIEDRA      VS      CONSOLA = TIJERA
        print(f" TU = {opcion_usuario}      VS       CONSOLA = {opcion_consola} \n  GANASTE")
        return 1
    elif opcion_usuario == "papel"  and opcion_consola == "piedra": #USUARIO = PIEDRA      VS      CONSOLA = PIEDRA
        print(f" TU = {opcion_usuario}      VS      CONSOLA = {opcion_consola} \n  GANASTE")
        return 1
    elif opcion_usuario == "tijera"  and opcion_consola == "papel": #USUARIO = TIJERA      VS      CONSOLA = PAPEL
        print(f" TU = {opcion_usuario}      VS        CONSOLA = {opcion_consola} \n  GANASTE")
        return 1

    # OPCIONES DE PERDER
    elif opcion_consola == "piedra" and opcion_usuario == "tijera": #CONSOLA = PIEDRA       VS      USUARIO = TIJERA
        print(f"TU  =    {opcion_usuario}       VS    CONSOLA =   {opcion_consola} \n  PERDISTE")
    elif opcion_consola == "papel" and opcion_usuario == "piedra": #CONSOLA = PAPEL       VS      USUARIO = PIEDRA
        print(f"TU  =   {opcion_usuario}        VS     CONSOLA  =   {opcion_consola} \n  PERDISTE")
    elif opcion_consola == "tijera" and opcion_usuario == "papel": #CONSOLA = TIJERA       VS      USUARIO = PAPEL
        print(f"TU  =    {opcion_usuario}       VS      CONSOLA =   {opcion_consola} \n  PERDISTE")