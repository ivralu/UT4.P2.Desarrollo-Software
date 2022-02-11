def inicializaJuego():
    palabra = str(input("Introduce la palabra secreta: "))
    return palabra
def defineLista(palabra):
    lista = []
    for i in range(0, len(palabra)):
        lista.append(False)
    return lista
def jugar(lista, palabra):
    for i in range(0, len(lista)):
        if(lista[i]==False):
            print('* ',end="")
        else:
            print(palabra[i:i+1] + " ", end="")
    print("")
    letra = str(input("Introduce una letra: "))
    return letra
def compruebaLetra(palabra, letra):
    if(palabra.find(letra)!=-1 and letra!=" "):
        return True
    return False
def listaCompleta(lista):
    enc = False
    for valor in lista:
        if(valor==False):
            enc=True


palabra = inicializaJuego()
lista = defineLista(palabra)
letrasIntroducidas = []
intentos = 6
while(intentos!=0):
    letra = jugar(lista, palabra)
    letrasIntroducidas.append(letra)
    if(compruebaLetra(palabra, letra)):
        print("La letra " + letra + " se encuentra en la posición " + str(palabra.find(letra)+1))
        lista[palabra.find(letra)]=True
    else:
        print("Has fallado!!!!")
    intentos-=1
if(intentos>0):
    print("Has acertado la palabra!!!")
else:
    print("Has perdido")

