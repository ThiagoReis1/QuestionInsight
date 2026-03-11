from numpy import*

v=array(eval(input("Registro: ")))
i=1
cont=0

while i < size(v):
	if v[i]>=v[0]:
		print(i)
		cont=cont+1
	i= i+1
print(cont)