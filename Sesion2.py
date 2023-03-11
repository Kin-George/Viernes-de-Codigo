#Variables

#Son objetos interpretables por python y cumplen la funcion de ser utilizados para interactuar con el sistema computacional.
#La funcion print sirve para imprimir los resultados o variables almacenadas en la terminal.

#Strings 
String1 = "me tiré el parcial" # el signo = en este caso es un operador de asignacion. 
String2 = 'SI APRENDO PYTHON INCREMENTARE MI SALARIO EN UN 200%'
String3 = "se puede utilizar todo tipo de caracter como string: ?@#, siempre sera leido como string, incluso numeros"

print(String1)
print(String2)
print(String3)
#Floats
Float1 = 10.22
Float2 = 10,2
float3 = 3.1463

print(Float1)
print(Float2)
print(float3)

#Boolean
boolean1 = True
boolean2 = False

print(boolean1)
print(boolean2)

#Enteros
entero1 = 10
entero2 = 5
entero3 = 10000000

print(entero1)
print(entero2)
print(entero3)

#Métodos para las variables
#String

print(String1.capitalize()) #Metodo para convertir en mayuscula la primera letra.
print(String1.upper()) #Metodo para convertir todo en mayuscula
print(String2.lower()) #Metodo para convertir todo en miniscula
print(String1.replace("tiré","quitaron")) #reemplaza una parte del texto por otra
print(String1.split()) #parte la frase 

# Conversion float - int
print(int(Float1))
print(float(entero1))

#Identificar la clase de una variable
print(type(String1))
print(type(Float1))
print(type(entero1))
print(type(boolean1))

#pedir ingreso de datos
nombre = input("Ingrese su nombre:")
print(f"Mucho gusto {nombre}")

#Ejercicio Variables

#Escriba un programa que solicite los siguientes datos: nombre, edad, programa, sexo, codigo. El nombre, programa y sexo debe ser en formato string.
#la edad y el codigo en formato entero. Luego, imprima en pantalla el nombre en mayuscula y el sexo es miniscula.

#Ingrese cualquier palabra como texto, y reemplace la vocal a por i.

#Estructuras de Datos
#Listas
lista = ['One piece','Naruto','DragonballZ']

#Acceder al elemento de la lista
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])

#Modificar la lista
lista[1] = 'HunterxHunter'
print(lista)

#Agregar elemento a la lista
lista.append("Bleach")
print(lista)

#Remover elemento
lista.remove("One piece")
print(lista)

#Diccionario
diccionario = {"nombre":"One piece","Autor":"Eichiro Oda"}
print(diccionario)
print(diccionario.values())
print(diccionario.keys())

#Actualizar diccionario
nuevoValor={"nombre":"HunterxHunter","Autor":"Togashi"}
diccionario.update(nuevoValor)
print(diccionario)

#Agregar elemento
diccionario["One piece"]="Eichiro Oda"
print(diccionario)

#Eliminar elemento
del diccionario["One piece"]
print(diccionario)

#tuplas
tupla = ('Jorge','Luisa','Esteban')
print(tupla)
print(tupla[1])

#Operaciones basicas

#suma
valor1 = 10
valor2 = 5
print(valor1+valor2)

#resta
print(valor1-valor2)

#multiplicacion
print(valor1*valor2)

#potencia
print(valor1**valor2)

#raiz
from math import sqrt #importar una libreria
print(sqrt(valor1**valor2))







