# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SQCQScvZNaNMSlqCRKnG7Lnu1tqUOsMJ
"""



"""SEMANA 05
1. Coleccion de datos
2. Estructuras Desicivas y Estructura Repetitivas
3. Clases y Objetos
4. Funciones

1. Coleccion de Datos
"""

#1.1 Listas
#Es una coleecion de elementos que puede ser ordenada, modificada, etc...
#Se identifica por los corchetes
#Ejemplo

aula = ["Huertas","Jimenez","Rodriguez","Caballero"]

aula

#podemos extraer cada elemneto por su posicion
print(aula[0])

#para agregar elementos a la lista
aula.append("Mamani")
aula.append("Fernandez")
aula

aula.remove("Huertas")
aula

#para eliminar un solo siempre escoge el de menor ubicacion
aula.remove("Mamani")
aula

#para recorrer podemos utilizar una estructura repetitiva
for alumno in aula:
  print(alumno)

#para invertir la lista utilizamos reverse()
aula.reverse()
aula

#para ordenar listas utilizamos sort()
aula.sort()
aula

##TUPLAS
tupla_aula = ("huertas","bravo","bonifacio","caballero")
tupla_aula

#conjuntos
conjunto_aula = {"huertas","bravo","bonifacio","caballero"}
conjunto_aula

#se puede recorrer utilizando una estructura repetitiva
for alumno in conjunto_aula:
  print(alumno)

#observacion no s epuede acceder por posicion pues no considera indexacion
conjunto_aula[2]

#para saber la cantidad de elementos len()
len(conjunto_aula)

#para agregar add()
conjunto_aula.add("Paye")
conjunto_aula

conjunto_aula.remove("bravo")
conjunto_aula

#diccionarios
#es una collecion de elementos, que estan indexados,
#no estan ordenados y se pueden modificar
#son escritos entre llaves y estan formados por pares de elementos
#INDICE:VALOR
diccionario_aula = {2:"huertas", '1':"bravo", 'dos':"bonifacio" ,'3':"caballero"}
diccionario_aula

#extraer el valor del diccionario
diccionario_aula["1"]

diccionario_aula["dos"]

#para añadir un par de elementos al diccionario hacemos
diccionario_aula["20"] = "velez"
diccionario_aula

#para eliminar un valor se utiliza pop() o del()
#por ejemplo, eliminar el elemento de indice dos ejemplo: para eliminar a Bernaoli
diccionario_aula.pop(2)
diccionario_aula

#para obtener el indice y el valor de cada elemento utilizamos items()
for indice, valor in diccionario_aula.items():
  print(indice,valor)

# 1.5. Ejercicio
# Dado una lista de [AMES, ARTEAGA , BARRIOS , BONIFACIO, BRAVO, CABALLERO , CAÑAZACA, FERNANDEZ , FLORES , GARCIA , HERRERA , HUERTA , HUERTAS, JIMENEZ , MAMANI , MANCILLA, PABLO , PAYE , PEÑA , PIZANGO, RAMOS, SANCHEZ,SEVILLANO, TINOCO, TORRES , VALDIVIESO, VELEZ , VILLANUEVA , ZUÑIGA]
# Diseñar un código que muestre si el apellido de un estudiante (Ingresado por teclado) forma parte de la lista
# tiempo: 12 minutos

alumnos = ["AMES", "ARTEAGA" , "BARRIOS" , "BONIFACIO", "BRAVO", "CABALLERO" , "CAÑAZACA", "FERNANDEZ" , "FLORES" , "GARCIA" , "HERRERA" , "HUERTA" , "HUERTAS", "JIMENEZ" , "MAMANI" , "MANCILLA", "PABLO" , "PAYE" , "PEÑA" , "PIZANGO", "RAMOS", "SANCHEZ","SEVILLANO", "TINOCO", "TORRES" , "VALDIVIESO", "VELEZ" , "VILLANUEVA" , "ZUÑIGA"]
nombre = input("Escribe el nombre del alumno")

if nombre in alumnos:
  print("El alumno ingresado si forma parte de la lista")
else:
  print("El alumno ingresado no esta dentro de la lista")