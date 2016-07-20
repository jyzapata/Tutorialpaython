'''
Created on 7/07/2016

@author: jamezaga
'''
# Definicion de funciones
def fib(n): # escribe la serie de Fibonacci hasta n
    """Escribe la serie de Fibonacci hasta n."""
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b
        
# Ahora llamamos a la funcion que acabamos de definir:
fib(2000)

#Funciones que retornan valor
def fib2(n): # devuelve la serie de Fibonacci hasta n
    """Devuelve una lista conteniendo la serie de Fibonacci hasta n."""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b) # ver abajo
        a, b = b, a+b
    return result
 
f100 = fib2(100) # llamarla
print "\n", f100 # escribir el resultado

def pedir_confirmacion(prompt, reintentos=4, queja='Si o no, por favor!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('s', 'S', 'si', 'Si', 'SI'):
            return True
        if ok in ('n', 'no', 'No', 'NO'):
            return False
        reintentos = reintentos - 1
        if reintentos < 0:
            raise IOError('usuario duro')
        print queja
        
pedir_confirmacion ('Realmente queres salir?')

