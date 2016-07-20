'''
Created on 7/07/2016

@author: jamezaga
'''

# IF
x = int(raw_input("Ingresa un entero, por favor: "))
if x < 0:
    x = 0
    print 'Negativo cambiado a cero'
elif x == 0:
    print 'Cero'
elif x == 1:
    print 'Simple'
else:
    print 'Mas'
    
# For
## Midiendo cadenas de texto
a = ['gato', 'ventana', 'defenestrado']
for x in a:
    print x, len(x)
    
for x in a[:]: # hacer una copia por rebanada de toda la lista
    if len(x) > 6: a.insert(0, x)

print a

## Iterar sobre numeros
print range(10)
print range(5, 10)
print range(0, 10, 3)
print range(-10, -100, -30)

## Iterar sobre indices de una secuencia
a = ['Mary', 'tenia', 'un', 'corderito']
for i in range(len(a)):
    print i, a[i]
    

