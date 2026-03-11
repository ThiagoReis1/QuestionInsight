from numpy import *
notas =  array (eval (input()))
pesos = array ([4,3])
s = notas * pesos
m = sum(s) / sum (pesos) 
print(round(m, 2))