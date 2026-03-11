from numpy import *

notas = array(eval(input( )))
a = size(notas) - min(notas)
print (round(a, 2))