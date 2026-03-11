from numpy import *
v= array (eval(input("digite as temperaturas:")))

i=0 # variavel contadora dos elementos
elementos=0
while (i<size(v)):
	if (v[i]>=0):
		elementos = elementos +1
	i=i+1
v0=array(zeros(elementos,dtype=float))
i=0
k=0 
while (i<size(v)):
	if (v[i]>=0):
		v0[k]=v[i]
		k= k+1
	i=i+1
print(v0)
		