# Asignatura: Funciones Básicas II
# Objetivos:
# Aprende a crear funciones básicas en Python
# Ponte cómodo usando listas
# Ponte cómodo haciendo que la función devuelva una expresión / valor


# 1 Cuenta regresiva : crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).
# Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]
lstctaregresiva =[]
def a(x):
    for x in range(x,-1,-1):
        lstctaregresiva.append(x)
    return lstctaregresiva

print(a(5))

# 2 Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo.
# Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2

lst=[1,2]

def imp1volv2(lst):
    print(lst[0])
    return lst[1]

print(imp1volv2(lst))

# 3 First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.
# Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)

lst=[1,2,3,4,5]
def devsum1l(lst):
    return (lst[0]+len(lst))
print(devsum1l(lst))

# 4 Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos, haga que la función devuelva False
# Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
# Ejemplo: values_greater_than_second ([3]) debería devolver False
vgts1 = [5,2,3,2,1,4]
vgts2 = [3]

def values_greater_than_second(vgts):
    if len(vgts) < 2:
        return False
    else:
        lista= []
        sgdoval = vgts[1]
        ct = 0
        for n in vgts:
            if n > sgdoval:
                lista.append(n)
                ct+=1
        print("la cuenta es ", ct)
        return lista

print(values_greater_than_second(vgts1))
print(values_greater_than_second(vgts2))

# 5 Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
# Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
# Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]


lenght = 4
valor = 7

def fnlst(l,v):
    lst=[]
    for i in range (1,l+1,1):
        lst.append(v)
    return lst

print(fnlst(lenght,valor))
lenght = 6
valor = 2
print(fnlst(lenght,valor))