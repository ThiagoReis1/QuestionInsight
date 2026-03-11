from numpy import *
notas = array(eval(input("notas :")))
m = sum(notas) - min(notas) 
n = size(notas) - 1
media = m / n
print(round(media,2))