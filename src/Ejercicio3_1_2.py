"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista
 y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.
"""
def fnduifis():
    sis=("Matematicas","Fisica","Quimica","Historia","Lengua")
    return sis

def main():
    sis=fnduifis()
    for puede in sis:  
        print(f"Yo estudio {puede}")

if __name__=="__main__":
    main()