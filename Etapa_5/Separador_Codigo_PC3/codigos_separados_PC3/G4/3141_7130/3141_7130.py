from numpy import*

n = array(eval(input("Numeros Reais Positivos: ")))
i = 0
g = 0

while(i < size(n)):
	g = g + n[i] ** (1/6)
	i = i + 1
t = (g/size(n))**6
print(round(t,2))