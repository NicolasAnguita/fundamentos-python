# Crea un archivo de Python llamado for_loop_basic1.py que realice las siguientes tareas.

# Básico : imprime todos los enteros del 0 al 150.
for x in range(151):
    print(x)

# Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
for x in range(5,1001,5):
    print(x)
    
# Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".
for x in range(1,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x%5==0:
        print("Coding")
    else:
        print(x)

# ¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
count = 1
sumaimpares =  0
while count < 500001:
    sumaimpares = sumaimpares+count
    count += 2
print("Suma final de enteros impares de 0 a 500.000 ", sumaimpares)


# Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.
positi = 2018
while positi > 0:
    print(positi)
    positi -=4
    
# Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)
lowNum = 2
highNum= 9
mult= 3

for x in range(lowNum,highNum+1,1):
    if x%mult == 0:
        print(x)

# BONUS: ¿Cómo se puede detectar si un número es primo? ¿Cómo retornar una lista con los primos entre el 1 y el 1000?

#aun no esta funcionando

# primos=[]

# for x in range(1,1001,1):
#     if x%x==0:
#         primos.append(x)

# print(primos)

