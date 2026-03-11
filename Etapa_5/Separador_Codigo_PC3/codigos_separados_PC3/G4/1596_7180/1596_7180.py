from numpy import *

nota = array(eval(input("Nota: ")))

#numerador
a = sum(nota)
b = min(nota)
c = a-b

e = size(nota) - 1

f = c/e

print(round(f,2))