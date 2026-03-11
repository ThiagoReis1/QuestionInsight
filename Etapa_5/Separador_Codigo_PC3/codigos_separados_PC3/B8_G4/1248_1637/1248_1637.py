#Universidade Federal do Amazonas
#Aluna: Ingrid de Lira Lima
#Exercicio: 01

from numpy import*
v= array(eval(input("digite: ")))
v1 = array (zeros(2, dtype= int))
a=min(v)
b=max(v)

c= (0.75*a)+(0.25*b)
d= 0.25*a + 0.75*b
for i in range(size(v)):
	if v[i]> c and v[i]<d:
		v1[0]=v1[0]+1
	elif v[i]>=d and v[i]<b:
		v1[1]=v1[1]+1
print(v1)	