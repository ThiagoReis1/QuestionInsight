from numpy import *
v = array(eval(input("velocidade: ")))
l = v[0] #limite de velocidade
m = 0 #quant de multas

for i in range(1,size(v)):
	a = l + l*0.2
	b = l + l*0.5
	if (v[i] > a and v[i] < b):
		print (i)
		m = m + 1

print(m)