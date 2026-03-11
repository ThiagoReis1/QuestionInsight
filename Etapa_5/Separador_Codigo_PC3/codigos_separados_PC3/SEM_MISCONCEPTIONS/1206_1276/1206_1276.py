from numpy import*
saltos = array(eval(input("Coloque os saltos: ")))
x = 8.95
i = 0
n = 0
while(i<size(saltos)):
	if(saltos[i]>x):
		n = n + 1
	i = i +1 
quantidade = ((size(saltos)) -n)
print(x)
print(quantidade)