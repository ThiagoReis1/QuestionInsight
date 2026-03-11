from numpy import *
nota = array(eval(input()))
peso = array([4,3])
m1 = nota[0]*peso[0] + nota[1]*peso[1]
m2 = peso[0] + peso[1]
media = m1/m2
print(round(media,2))