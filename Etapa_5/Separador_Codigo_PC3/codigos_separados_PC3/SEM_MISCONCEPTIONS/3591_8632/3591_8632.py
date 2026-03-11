from numpy import*

v = array(eval(input("v: ")))
i = 0
pontos = 0
while i < size(v):
	if (v[i]%2)== 0:
		pontos = pontos + 5
	else:
		pontos = pontos + 10
	i = i + 1
print(pontos)