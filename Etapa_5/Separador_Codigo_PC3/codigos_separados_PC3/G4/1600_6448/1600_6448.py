from numpy import*

v=array(eval(input("Valor dos itens: ")))

i=0
x=0
while i < size(v):
	if v[i]>80:
		x = x + v[i] * 0.15
	i=i+1
print(round(sum(v)-x,2))