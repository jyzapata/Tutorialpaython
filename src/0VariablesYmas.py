'''
Created on 6/07/2016

@author: jamezaga
'''
# Declarar variables
hola = "james"
# Declarar variables con asignacion multiples multiples
a, b = 0, 1

print hola;
print hola [-1]
print len(hola)

# Declarar listas
a = ['pan', 'huevos', 100, 1234]
print a

## Fibonaci impresa verticalmente
a, b = 0, 1
while b < 10:
    print b
    a, b = b, a+b

## Fibonaci impresa horizontalmente
a, b = 0, 1
while b < 10:
    print b,
    a, b = b, a+b    

i = 256*256
print '\nEl valor de i es', i, 'y el de b es', b   