from numpy import*

c = array(eval(input("Tempo de Chegada em Segundos: ")))
i = 0
v = c[i]
n = 0

while i < size(c):
	if v < c[i]:
		v = c[i]
		n = i
	i = i + 1
print(n)