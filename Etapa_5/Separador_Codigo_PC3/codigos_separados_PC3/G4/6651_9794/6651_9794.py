from numpy import*
notas = array(eval(input("Insira as notas: ")))
p = array([5, 4, 3, 2])
i = 0
n = 0
d = 0
while i < size(notas):
	n = n + (notas[i] * p[i])
	d = d + p[i]
	i = i + 1
c = n / d
print(round(c, 2))
