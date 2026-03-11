from numpy import *

notas = array(eval(input("insira as 3 notas:")))
pesos = array([2,1,5])

num = notas * pesos

m = sum(num) / sum (pesos)
print(round(m, 2))