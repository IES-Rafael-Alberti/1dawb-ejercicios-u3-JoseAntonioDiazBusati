"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""
"""
def PedirNumero():
    BoletoGanador=[]
    cont=6
    while cont!=0:
        numero=int(input("Introduce los numeros ganadores: "))
        try:
            if numero<=49 and numero>=1:
                BoletoGanador.append(numero)
                cont-=1
            else:
               raise ValueError
        except ValueError:
            print("***Tiene que ser un numero entre 1-49 o no ser iguales***")
    return BoletoGanador

def PedirReintegro():
    reintegro==True
    while reintegro!=False:
        reintegro=int(input("Introduzca el numero de reintegro: "))
        try:
            if reintegro>=0 and reintegro<=9:
                reintegro==False
            else:
                reintegro==True
                raise ValueError
        except:
            print("***Solo puede ser un numero entr 0-9***")
    return reintegro

def main():
    sis=PedirReintegro()
    return print(sis) 
    
if __name__=="__main__":
    main()

"""