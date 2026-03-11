from numpy import*
v = array(eval(input("Digite o tempo de chegada: ")))
i = 0

while i < size(v):
	if v[i] == min(v):
		print(i)
	i = i + 1