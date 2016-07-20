'''
Created on 12/07/2016

@author: jamezaga
'''

def ventadequeso(tipo, tipo2, *argumentos, **palabrasclaves):
    print "-- Tiene", tipo, "?"
    print "-- Lo siento, nos quedamos sin", tipo
    for arg in argumentos:
        print arg
    print "-"*40
    claves = palabrasclaves.keys()
    claves.sort()
    for c in claves:
        print c, ":", palabrasclaves[c]
     
     
ventadequeso("Limburger", "Es muy liquido, sr.",
             "Realmente es muy muy liquido, sr.", "Realmente es muy muy liquido, sr.",cliente="Juan Garau",vendedor="Miguel Paez",puesto="Venta de Queso Argentino",puesto2="Venta de Queso Argentino")
