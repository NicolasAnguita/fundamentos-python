# Asignatura: Funciones Intermedias II

# Objetivos:

# Practica escribir funciones y recorrer los diccionarios
# Comprender mejor cómo recorrer una lista de diccionarios o un diccionario de listas
# Nota: Evita usar palabras clave de clase como int, str, list y dict como nombres de variables / parámetros.

# A) Actualiza los valores en diccionarios y listas

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1 Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
x[1][0]=15
print(x)

# 2 Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
students[0]["last_name"]= "Bryant"
print(students[0])


# 3 En el directorio sports_directory, cambia 'Messi' a 'Andres'
sports_directory["soccer"][0] = "Andress"
print(sports_directory["soccer"])


# 4 Camba el valor 20 en z a 30
z[0]["y"]=30
print(z)

#  B) Itera a través de una lista de diccionarios

# Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios, la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado. Por ejemplo, dada la siguiente lista:
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(lst):
    for d in students:
        print(f'first_name - {d["first_name"]}, last_name - {d["last_name"]} ')

iterateDictionary(students) 
# La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)

# Bonus: Hacer que aparezcan exactamente así!

# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#  C) Obtén valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. 
# Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:
# Michael
# John
# Mark
# KB
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    for student in students:
        print(student[key_name])
        
iterateDictionary2 ('first_name', students)
iterateDictionary2('last_name', students)

#  D) Itera a través de un diccionario con valores de listas
# Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for v in some_dict:
        print(len(some_dict[v]), v)
        for el in some_dict[v]:
            print(el)

printInfo(dojo)
