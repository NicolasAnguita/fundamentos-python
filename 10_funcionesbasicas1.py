#Para cada uno de los siguientes fragmentos de código, primero prediga la salida (lo que verá impreso en el terminal). Una vez que hayas hecho una predicción, ejecuta el fragmento de código para ver si estás en lo correcto.

#1
def a():
    return 5
print(a())
# Prediccion: 5

#2
def a():
    return 5
print(a()+a())
# Prediccion: 10

#3
def a():
    return 5
    return 10
print(a())
# Prediccion: 5

#4
def a():
    return 5
    print(10)
print(a())
# Prediccion: 5

#5
def a():
    print(5)
x = a()
print(x)
# Prediccion: 5, NONE

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
# Prediccion: 3,5, funcion a en realidad no devuelven nada, no tiene return

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# Prediccion: 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# Prediccion: 100, 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# Prediccion: 7,14, 21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
# Prediccion: 8


#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
# Prediccion: 500, 500, 300, 500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
# Prediccion: 500, 500, 300, 500

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
# Prediccion: 500, 500, 300, 300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# Prediccion: 1, 3, 2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# Prediccion: 1, 3, 5, 10