# coding=UTF-8
# Viega Ruiz, Ismael

def solicitaPalabraSecreta():
    numAciertos = []

    palabraSecreta = input("\nIntroduce la palabra secreta: ")

    for i in range(len(palabraSecreta)):
        numAciertos.append(False)

    return palabraSecreta,numAciertos

def muestraPalabraSecreta(palabraSecreta, numAciertos):
    indice = 0
    palabra = ""

    for acierto in numAciertos:
        if acierto:
            palabra = palabra + palabraSecreta[indice]
        else:
            palabra = palabra + "*"
        
        indice += 1
    
    print("Palabra Secreta: " + palabra)
    print("")

def solicitaLetra(letrasIntroducidas):
    while True:
        letra = input("Introduce una sola letra: ")

        if len(letra) != 1:
            print("Por favor, solo una letra.")
        else:
            break

    letrasIntroducidas = letrasIntroducidas + letra + " "
    return letra, letrasIntroducidas

def compruebaPalabraSecreta(letraIntroducida, palabraSecreta, numAciertos):
    haAcertado = False

    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] == letraIntroducida:
            numAciertos[i] = True
            haAcertado = True

    return haAcertado, numAciertos

def muestraDibujo(numFallos):
    print("\nDibujo:")

    if numFallos == 1:
        print("------")
        print("|   |")
        print("|   o")
        print("|  ")
        print("|  ")
        print("_________")

    elif numFallos == 2:
        print("------")
        print("|   |")
        print("|   o")
        print("|  /|")
        print("|")
        print("_________")
        
    elif numFallos == 3:
        print("------")
        print("|   |")
        print("|   o")
        print("|  /|\\")
        print("|")
        print("_________")

    elif numFallos == 4:
        print("------")
        print("|   |")
        print("|   o")
        print("|  /|\\")
        print("|  / ")
        print("_________")
        
    elif numFallos == 5:
        print("------")
        print("|   |")
        print("|   o")
        print("|  /|\\")
        print("|  / \\")
        print("_________")
        
    print("")

print("Bienvenido a 'AHORCADO'.")
print("Pd: Tienes 5 intentos para adivinar la palabra secreta.")
numFallos = 0
letrasIntroducidas = ""
palabraSecreta, numAciertos = solicitaPalabraSecreta()

while True:
    muestraPalabraSecreta(palabraSecreta, numAciertos)
    
    if numFallos != 0:
        muestraDibujo(numFallos)
        print("-----------------------------------------")
        print("Letras introducidas: ", letrasIntroducidas)
        
    letra, letrasIntroducidas = solicitaLetra(letrasIntroducidas)
    acierto, numAciertos = compruebaPalabraSecreta(letra, palabraSecreta, numAciertos)

    if not acierto:
        numFallos = numFallos + 1

    if numAciertos.count(True) == len(palabraSecreta) or numFallos == 5:
        break
    
if numFallos == 5:
    muestraPalabraSecreta(palabraSecreta, numAciertos)
    muestraDibujo(numFallos)

    print("\nVaya, se te han acabado las oportunidades. Has perdido.")
else:
    print("\n¡Enhorabuena! Has ganado.")