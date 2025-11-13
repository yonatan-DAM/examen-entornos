'''
Programa realizado por Yonatan Mora (c)2025
Este programa aplica el concepto de CRUD a la base de datos llamada
portafolioexamen REFACTORIZADO a un archivo externo mediante la llamada
del archivo base llamado examen1.py
siguiendo las mismas funciones que el archivo original

C = Crear
R = Leer
U = Actualizar
D = Eliminar
'''
import examen1               # importamos el archivo princial

def menuPrincipal():         # creamos la funcion del menu para llamar directamente al menu principal
   
    examen1.menuPrincipal()  # a examen1 le asignamos la funcion anteriormente creada

if __name__ == "__main__":   # con esta estructura nos aseguramos ejecutar el programa principal y no otro
    menuPrincipal()          # llamada al menu principal

'''
✅ Conclusion:

Esta refactorizacion demuestra la capacidad de construir un programa en funciones y luego llamarlas a un
archivo externo para su completa ejecucion y funcionamiento
'''