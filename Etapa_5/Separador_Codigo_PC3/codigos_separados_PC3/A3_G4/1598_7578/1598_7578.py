from numpy import *

c=array(eval(input("custo dos itens ")))
i=0
d=float(-6.50)
t=c

if all(c)>90:
	t=(c-6.50)
else:
	t=c
i=+1
p=(sum(t))
print(round(p,2))
	
