"""
Created on Mon May 30 11:50:20 2022

@author: CARLOS RUIZ MONTERO
"""
import os
def crear_archivo(nombre, contenido):
    archivo = open(nombre,"wt")
    archivo.write(contenido)
    archivo.close()

def eliminar_archivo(nombre):
    os.remove(nombre)
    
