from numpy import *
notas = array(eval(input("Notas: ")))

n = shape(notas)[0]
a = sum(notas)
b = min(notas)
c = (a - b) / (n - 1)

#print(a)
#print(c)
print(round(c,2))