from numpy import *

v = array(eval(input()))
somasup = 0
tamanho = len(v)

for i in v:
	somasup = somasup + exp(i)

m = log(somasup/exp(tamanho))

m = round(m, 2)

print(m)