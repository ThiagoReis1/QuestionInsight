from numpy import*

a = array(eval(input("aneis acertados: ")))

i = 0
pontos = 0

while i < size(a):
	if a[i] == 1:
		pontos = pontos + 100
	elif a[i] == 2:
		pontos = pontos + 60
	elif a[i] == 3:
		pontos = pontos + 20
	else:
		pontos = pontos
	i = i + 1
print(pontos)
		