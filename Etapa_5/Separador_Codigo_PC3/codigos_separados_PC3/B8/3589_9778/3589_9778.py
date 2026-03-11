from numpy import*

aneis = array(eval(input("acertos: ")))

i=0
pontos = 0

while i < size (aneis):
	if aneis [1] == 1:
		pontos += 80
	elif aneis [i] == 2:
		pontos += 40
	elif aneis [i] == 3:
		pontos += 20
	elif aneis [i] == 4:
		pontos += 10
	i+=1
print(pontos)