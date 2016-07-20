'''
Created on 10/07/2016

@author: jamezaga
'''

i = 5

def f(arg=i):
    print arg
    i= 4
    print i
    
i = 6
print i
f()

