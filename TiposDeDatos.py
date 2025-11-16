
#Tipos de Datos en python y como declararlos 

#!Numeros
#? Enteros = Int 
x = 10
#? Flotantes = float
pi = 3.1416
#?Complejos = complex
z = 3 + 5j

#!Cadenas de texto = str
#? Reprecentan verdadero o falso 
nombre = "Juan "
saludo = 'Hola Mundo'
#? Multilineas
texto = """ esto 
    es una cadena 
    de texto """

#!Booleanos = bol
#? Representan Vardadero o Falso
Activo = True
es_Mayor= False

#!Listas = list
#? Coleccion ordenada y modificable
numeros = [1,2,3,4]
mixta= [10,"hola",True,3.1234] 
# ? listas vacias 
vacia= []

#!Tuplas = tuple
#? coleccion ordenada pero inmutable 
cadena= (10,20)
datos = ("Juan", 25, "México")
#? tuplas de un solo elemento
tupla= (3,)

#! Conjuntos = set
#? coleccion no ordenada, sin elementos duplicados 
colores= {"Rojo", "Azul", "Verde"}
#? conjuntos vacios 
vacio= set()

#!Diccionarios= dict
#? coleccion de datos en formato clave :Valor
persona= {
    "nombre": "luis",
    "edad":30,
    "Ciuda": "Madrid"
}
#! None Type = none
#? Representa ausencia de valor 
resultado = None

#TODO: Ejercicos Practicas 
#* Variables de distintos Tipos
#? Int
x= 34
#? Float
j= 134.23
#? str
hola= "hola mundo "
#? bool
verdadero= True
print (x, ",", j,",",hola ,",",verdadero )

#* Cracion de listas 
lista= [1,2, 3, 4]
print ("\n", lista)

#*Diccionarios 
diccionario= {
    "Nombre":"Eduardo",
    "edad": 20,
    "Mmunicipi":"Chapa de Mota"
}
print (diccionario)
#* Conjuntos con repeticion
colores= {"rojo", "rojo", "azul", "verde"}
print(colores)
