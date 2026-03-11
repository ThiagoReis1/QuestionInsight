from numpy import*
v = array(eval(input("v:")))
i = 0
pontos = 100
while i < sum(v):
	if i == 1:
		pontos = pontos * 5
	elif i == 2:
			pontos = pontos * 3
	elif i == 3:
		pontos = pontos 
	elif i == 4: 
		pontos = pontos / 2
	i = i + 1
print(round(pontos, 2))