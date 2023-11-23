"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es
cada una de las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""
def LasAsignaturas():
    asig=("Matematicas","Fisica","Quimica","Historia","Lengua")
    return asig

def Pedirnotas():
    nota=[]
    return nota

def main():
    asignatura=LasAsignaturas()
    notas=Pedirnotas()
    i=0
    while i:
        note=int(input(f"Introduce la nota de {asignatura[i]}:"))
        notas.append(note)
        i+=1
    while i:
        print(f"En {asignatura[i]} has sacado un {notas[i]}")
        i+=1

if __name__=="__main__":
    main()