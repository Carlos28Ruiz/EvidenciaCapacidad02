# -*- coding: utf-8 -*-
"""
Created on Mon May 30 19:36:53 2022

@author: CARLOS
"""
import gestion_archivos

def menu():
    print("*****MENU PRINCIPAL*****")
    print("1. Crear archivo")
    print("2. Eliminar archivo")
    print("3. Agregar contenido")
    print("4. Mostrar contenido del archivo")
    print("5. Salir")

def crear():
    print("--Crear Archivo--")
    archivo  = input("Archivo: ")
    contenido = input("Contenido: ")
    gestion_archivos.crear_archivo(archivo, contenido)
    
def eliminar():
    print("--Eliminar Archivo")
    archivo = input("Archivo: ")
    gestion_archivos.eliminar_archivo(archivo)

def agregar():
    print("--Agregar Datos a un archivo--")
    archivo = input("Archivo: ")
    contenido = input("Contenido: ")
    gestion_archivos.agregar_contenido_archivo(archivo, contenido)
    
def listar():
    print("--Mostrar contenido de un archivo--")
    archivo = input("Archivo: ")
    print(gestion_archivos.leer_archivo(archivo))

