from numpy import *

v = array(eval(input("Digite os valores sacados: ")))
t = size(v)
cont = 0
j = 0
for i in v:
	if i <= 50 :
		cont = cont + 1
x = zeros(cont,dtype=int)
for i in range(t):
	if v[i] <= 50:
		x[j] = i 
		j = j + 1
		
		
print(cont)
print(x)