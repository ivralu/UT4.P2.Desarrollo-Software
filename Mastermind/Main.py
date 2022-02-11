# coding=UTF-8
# Viega Ruiz, Ismael

import random

def generaNumAleatorio():
    num1, num2, num3, num4 = random.sample("0123456789", 4)
    numAleatorio = []
    
    numAleatorio.append(str(num1))
    numAleatorio.append(str(num2))
    numAleatorio.append(str(num3))
    numAleatorio.append(str(num4))
    
    return numAleatorio

def solicitaNum():
    numUsuario = []
    
    print("\n--------------------------------------")
    
    while len(numUsuario) < 4:
        cifraRepetida = False
        numUsuario = []
        num = ""
        
        while cifraRepetida == False and len(num) < 4 or len(num) > 4:
            num = str(input("Introduzca un número de 4 cifras: "))
            
            if len(num) < 4 or len(num) > 4:
                print("Debe introducir un número entero de sólo 4 cifras.\n")
        
        for i in num:
            if i not in numUsuario:
                numUsuario.append(str(i))
            else:
                cifraRepetida = True
                break
            
        if cifraRepetida == True:
            print("Has introducido una o más cifras repetidas.")
            print("Vuelva a intentarlo.\n")
            
    print("--------------------------------------")
    return numUsuario
    
def compruebaJuego(numAleatorio, numUsuario):
    numResuelto = ["*", "*", "*", "*"]
    muertos = 0
    heridos= 0
        
    for i in range(0, len(numAleatorio)):
        for j in range(0, len(numUsuario)):
            if numAleatorio[i] == numUsuario[j]:
                if i == j:
                    muertos = muertos + 1
                    numResuelto.pop(i)
                    numResuelto.insert(i, numAleatorio[i])
                    print(" - Número '" + str(numUsuario[j]) + "' MUERTO en la posición " + str(i + 1))
                else:
                    heridos = heridos + 1
                    print(" - Número '" + str(numUsuario[j]) + "' HERIDO en la posición X")
    
    return muertos, heridos, numResuelto

resultadoPartidas = []   
numAleatorio = generaNumAleatorio()
numIntentos = 1

print("Bienvenido a 'MASTERMIND'.")

while True:
    numUsuario = solicitaNum()
    print("\n------ NÚMERO INTRODUCIDO: " + str("".join(numUsuario)) + " ------\n")
    
    muertos = 0
    heridos = 0
    
    muertos, heridos, numResuelto = compruebaJuego(numAleatorio, numUsuario)
    print("\n-------- NÚMERO SECRETO: " + str("".join(numResuelto)) + " --------")
    
    if muertos == 4:
        print("\n--------------------------------------\n")
        print("¡ ENHORABUENA !")
        print("Has adivinado el número secreto.")
        print("Número de Intentos: " + str(numIntentos))
        break    
    
    numIntentos = numIntentos + 1
