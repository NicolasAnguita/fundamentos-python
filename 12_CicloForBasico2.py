# Asignatura: Ciclo For Básico II
# Objetivos:
# Obten funciones de escritura cómodas solo usando bloques de construcción básicos de Python (es decir, usando sus propias habilidades en lugar de confiar en los elementos integrados)
# Ponte cómodo usando bucles, funciones, listas y otros tipos de datos

# Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
# Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]

testlst = [-1, 3, 5, -5]
def positobig(lst):
    for i in range(0,len(lst)):
        print(i)
        if lst[i] > 0 :
            lst[i] = "big"
    return lst
print(positobig(testlst))

# Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
# Ejemplo: count_positives([- 1, 1, 1,1 ]) cambia la lista original a [-1, 1, 1, 3] y la devuelve
# Ejemplo: count_positives([1, 6, -4, -2, -7, -2]) cambia la lista a [1, 6, -4, -2, -7, 2] y la devuelve

lstnume1 = [- 1, 1, 1, 1]
lstnume2 = [1, 6, -4, -2, -7, -2]
count = 0

def count_positives(lst):
    count = 0
    for i in range(0, len(lst)):
        if lst[i] > 0:
            count += 1
    lst[len(lst)-1] = count
    return lst

print(count_positives(lstnume1))
print(count_positives(lstnume2))

# Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
# Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
# Ejemplo: sum_total ([6,3, -2]) debería devolver 7

lista1 = [1,2,3,4]
lista2 = [6,3, -2]

def sum(lst):
    suma = 0
    for val in lst:
        suma += val
    return suma

# print(sum(lista1))
# print(sum(lista2))

# Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
# Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

lista1 = [1,2,3,4]

def promedio(lst):
    suma = 0
    for val in lst:
        suma += val
    return (suma/len(lst))

# print(promedio(lista1))

# Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
# Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
# Ejemplo: longitud ([]) debería devolver 0


lista1 = [37,2,1, -9]
lista2 = []

def longitud(lst):
    return len(lst)

# print(longitud(lista1))
# print(longitud(lista2))

# Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
# Ejemplo: mínimo ([]) debería devolver False

lista1 = [37,2,1, -9]
lista2 = []

def minimo(lst):
    min=0
    if len(lst)==0:
        return False
    else:
        for val in lst:
            if val < min:
                min = val
        return min

# print(minimo(lista1))
# print(minimo(lista2))


# Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
# Ejemplo: máximo ([]) debería devolver False

lista1 = [37,2,1, -9]
lista2 = []

def maximo(lst):
    max = 0
    if len(lst)==0:
        return False
    else:
        for val in lst:
            if val > max:
                max = val
        return max

# print(maximo(lista1))
# print(maximo(lista2))


# Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
# Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}

lista = [37,2,1, -9]

def ultimate_analysis(lst):
    return { "total": sum(lst),
            "promedio": promedio(lst),
            "minimo": minimo(lst),
            "maximo": maximo(lst),
            "longitud": longitud(lst)
    }

print(ultimate_analysis(lista))

# Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]

lista = [37,2,1, -9]

def reverse_list(lst):
    medio = len(lst)//2
    for i in range(0, medio):
        temp = lst[i]
        lst[i] = lst[len(lst)-1-i]
        lst[len(lst)-1-i] = temp
    return lst

print(reverse_list(lista))
