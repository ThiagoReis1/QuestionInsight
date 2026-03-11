from numpy import *
vdanos=array(eval(input("")))
p=0 #peso de cada ataque
a=0 #acumulador de danos
i=0 #variavel contadora
d=0
while(i < size(vdanos)):
	a= vdanos[i] * (p+1)
	i=i+1
	p= p + 1
	d= a + d
i + 1
print(d)