pontos = 100

aneis = eval(input())

i = 0

while i < len(aneis):
	if aneis[i] == 1:
		pontos *= 5
	elif aneis[i] == 2:
		pontos *= 3
	elif aneis[i] == 4:
		pontos /= 2
	i += 1

print(round(pontos,2))