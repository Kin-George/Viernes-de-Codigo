#Operadores de asignacion
x = 100
print(x)
x+=10
print(x)
x-=20
print(x)
x*=5
print(x)
x/=10
print(x)
x**=2
print(x)
print("-"*100)

#Operadores de comparación
y = 100
#Mayor que
print(y>100)
#Mayor o igual que
print(y>=100)
#Menor que
print(y<100)
#Menor o igual que
print(y<=50)
#Igual
print(y==100)
#Distinto
print(y!=100)
print("-"*100)

#Condicionales
numero=int(input("Ingrese el numero:"))
if numero%2==0:
    print(f"el numero {numero}, es par")
else:
    print(f"el numero {numero}, es impar")

ingresos=int(input("dinero disponible:"))
if ingresos<25000:
    print(f"Tienes para una salida simple; un heladito y poco mas.")
elif ingresos<100000:
    print(f"Tienes para una salida decente; una salchipapa con su bebida.")
else:
    print(f"Tienes para una salida en condiciones; infinidad de posiblidades.")

referencia="JORGE M. OROZCO"
comprobante=input("Digite su nombre:")
if comprobante==referencia:
    print(f"Acceso concedido")
else:
    print(f"¿Quien tu eres?. Acceso denegado")
print("-"*100)

#Operadores logicos
valor1=10
valor2=100
if valor1 or valor2 == 10:
    print(f"me sirven esas cantidades")
else:
    print(f"No me sirven esas cantidades")

titulo = input("Ingrese su titulo profesional:")
habPrograma = input("Sabe programar: Si o No:")
if titulo.lower() == "economista" and habPrograma.lower()=="si":
    print("Estas contratado!")
else:
    print("Nosotros te llamamos")

a = "Pescado"
comida = input("Ingrese el tipo de comida:")
if not comida.lower() == a:
    print(f"No es pescado")
else:
    print(f"Es pescado")
print("-"*100)

#Operadores de pertenencia
listaEstudiantes=[]
for i in range(10):
    nombres=input("Ingrese el nombre del estudiante:")
    listaEstudiantes.append(nombres)
print("Jorge" in listaEstudiantes)
print("Jorge" not in listaEstudiantes)
print("-"*100)

#Bucles 
i=1
while i < 10:
    print(f"Esto es un bucle con while.")
    i+=1

for i in range(10):
    print(f"Esto es otro bucle, pero con for")
print("-"*100)

#Funciones
def suma(valor1,valor2):
    return valor1+valor2
print(f"El resultado de la suma es:", suma(1,5))










