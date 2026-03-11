from math import*
x = int(input("numero fornecido pelo usuario: "))
numero1= x//1000
numero2= x%1000

c=(numero1-numero2)**2
if(c==x):
	m= "atende"
else:
	m= "nao atende"
print(m)
print(x)