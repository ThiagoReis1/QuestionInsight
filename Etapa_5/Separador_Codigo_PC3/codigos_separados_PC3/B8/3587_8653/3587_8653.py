from numpy import*
num = array(eval(input()))
pontos = 100
i = 0
while i < size(num):
	if num[i] == 1:
		pontos = pontos * 5
	elif num[i] == 2:
		pontos = pontos * 3
	elif num[i] == 4:
		pontos = pontos / 2
	i = i + 1
print(round(pontos, 2))
	