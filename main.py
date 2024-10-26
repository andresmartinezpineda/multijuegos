import piedra_papel.piedra_papel_tijera as piedra_papel_tijera#importamos la carpeta piedra papel
import adivinando_numero.adivina_numero as adivina_numero#importamos la carpeta adivinando_numero

escoger_juego = int(input("Elige uno de los siguientes juegos:\n1. piedra, papel o tijera\n2. adivina el numero\n"))
"""le indicamos al usuari que ingrese un numero para elegir el juego"""

if escoger_juego == 1: #si el usuario escoge 1 se llamara a la funcion (piedra_papel_tijera)
    piedra_papel_tijera.piedra_papel_tijera()#esta se encuentra en la carpeta (piedra_papel_tijera)
elif escoger_juego == 2:#si el usuario escoge 1 se llamara a la funcion (adivina_numero)
    adivina_numero.adivina_numero()#esta se encuentra en la carpeta (adivinando_numero)