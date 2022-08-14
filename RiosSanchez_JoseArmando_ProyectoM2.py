frase = input("Ingresa una frase con mínimo 4 letras y máximo 8: ")

while not frase.isalpha() :    #Validamos mediante isalpha solo tengamos letras en la cadena
    print("La frase solo debe contener letras. Intente de nuevo")  #Y el ciclo se repite mientas no
    frase = input("Ingresa una frase con mínimo 4 letras y máximo 8: ") #se cumpla esta condicion


flag = "1"    #Flag es una bandera que controla el ciclo de revision de la cadena escrita

while flag == "1":
    if len(frase) == 1 :    #Caso 1 la frase tiene menos de 4 letras
        print(f"Hacen falta letras. Sólo tiene {len(frase)} letra.")
    elif len(frase) < 4:   #Subcaso del caso uno: solo hay una letra en la frase
        print(f"Hacen falta letras. Sólo tiene {len(frase)} letras.")
    elif len(frase) > 8 :   #Caso 2 la frase tiene mas de 8 letras.
        print(f"Sobran letras. Tiene {len(frase)} letras")
    
                            #caso 3 la frase tiene entre 4 y 8 letras
    elif len(frase)>=4 and len(frase)<=8 :
        print(f"La frase es {frase}. La frase es correcta")
    
    flag = input("¿Desea comprobar otra frase? (1) Si (2) No     ")  #LA bandera controla la repeticion

    if flag == "1":

        frase = input("Ingresa una frase con mínimo 4 letras y máximo 8: ")
        while not frase.isalpha() :
            print("La frase solo debe contener letras. Intente de nuevo")
            frase = input("Ingresa una frase con mínimo 4 letras y máximo 8: ")
    elif flag== "2":
        print("Eligio terminar el programa.")
        continue #AQUI MODIFIQQUE ESTA SALIDA DEL PROGRAMA ORIGINAL PAR PODDER ENTRAR AL PROGRANA DE COORDENADAS
    else:
        print("Opcion invalida. Se cerrará el programa.")
        exit()

    



flag = "1"

while flag == "1":
    while True:           #Usamos un ciclo para validar el dato ingresado mediante el error generado
        try:              #via la conversion usando int,mediante la estructura Try except
            coordenadaX =int(input("Ingrese el valor de X: ")) 
            if coordenadaX == 0:                      #si no genera error, validamos si el valor es 0, 
                print("El valor de X no puede ser 0")
            elif coordenadaX < 0:
                print("El valor de X es negativo")     #si el numero es negativo
                break
            elif coordenadaX > 0:
                print("El valor de X es positivo")     #o si es positivo. Ambos casos sacan del ciclo.
                break

        except:   #Si se genera el error, se maneja aqui y se avisa que el valor no es válido. Reinicia.
            print("No has ingresado un numero valido para X")


    while True:     #Ejecuta la misma validacion para la coordenada Y
        try:
            coordenadaY =int(input("Ingrese el valor de Y: "))
            if coordenadaY == 0:
                print("El valor de Y no puede ser 0")
            elif coordenadaY < 0:
                print("El valor de Y es negativo")
                break
            elif coordenadaY > 0:
                print("#El valor de Y es positivo")
                break

        except:
            print("No has ingresado un numero valido para Y")


    coordenada = [coordenadaX, coordenadaY] #Ingresamos los valores en una lista, para un par ordenado

    #El par ordenado es evaluado en su valor numerico para determinar el cuadrante correspondiente.
    if coordenada[0] > 0 and coordenada[1] > 0 :
        print("El punto se encuentra en el Cuadrante I")
    elif coordenada[0] < 0 and coordenada[1] > 0 :
        print("El punto se encuentra en el Cuadrante II")
    elif coordenada[0] < 0 and coordenada[1] < 0 :
        print("El punto se encuentra en el Cuadrante III")
    elif coordenada[0] > 0 and coordenada[1] < 0 :
        print("El punto se encuentra en el Cuadrante IV")

    flag = input("¿Desea comprobar otra coordenada? (1) Si (2) No   ")  #LA bandera controla la repeticion
    if flag == "2":
        print("Eligió terminar el programa.")
        exit()
    elif flag == "1":
        continue    
    else:
        print(f"opcion inválida.", end = "\n")
        while flag != "1" and flag != "2":  #Reducimos el ciclo a dos opciones posibles
            flag = input("¿Desea comprobar otra coordenada? (1) Si (2) No   ")  #LA bandera controla la repeticion




