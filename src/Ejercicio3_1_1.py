"""
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""
def AsignaturasTotales():
    asignatura=[]
    asig=""
    cont=0
    while asig!= ".":
        asig=str(input("Añade tus asignaturas de una en una: "))
        asignatura.append(asig)
        cont+=1
    return asignatura

def main():
    asignatura=AsignaturasTotales()
    for asig in asignatura:
        print(asig)
    return asig
    
if __name__=="__main__":
    main()