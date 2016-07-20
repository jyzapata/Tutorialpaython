'''
Created on 12/07/2016

@author: jamezaga
'''
def loro(tension, estado='muerto', accion='explotar', tipo='Azul Nordico'):
    print "-- Este loro no va a", accion,
    print "si le aplicas", tension, "voltios."
    print "-- Gran plumaje tiene el", tipo
    print "-- Esta", estado, "!"
    print ""
    
loro(100)

d = {"tension": "cuatro millones", "estado": "demacrado", "accion": "VOLAR"}

loro(**d)


print range(3, 6)


args = [3, 6]
print range(*args)