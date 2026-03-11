from numpy import*
from math import*
a = float(input("digite"))
b = array(eval(input("digite")))
c = array(eval(input("digite")))
cont=zeros(2,dtype=(int))
t=(a/a-1)
soma =0
for i in range(size(b)):
	soma =soma + abs(b[i] - c[i])**t			
	raiz =soma ** (1/t)		
print(round(raiz,6))
					
	