from numpy import * 
np = array(eval(input("Digite nomes dos produtos: ")))
qt = array(eval(input("Digite as quantidades dos produtos: ")))
c = 0
a = 0
fe = 0
b = 0
m = 0
f = 0
while (c < size(np)):
	if np[c] == "ARROZ":
		a=a+qt[c]*1.25
	elif np[c] == "FEIJAO":
		fe=fe+qt[c]*2.60 
	elif np [c] == "BIS":
		b=b+qt[c]*1.80
	elif np [c]== "MIOJO":
		m=m+qt[c]*0.85
	elif np [c]== "FANTA":
		f=f+qt[c]*3.20
	c+=1
soma = a+fe+b+m+f
print(round(soma, 2))
