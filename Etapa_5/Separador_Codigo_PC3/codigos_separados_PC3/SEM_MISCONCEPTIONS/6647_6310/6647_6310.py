from numpy import sum
pesos = [2.0,1.0,5.0]
notas = eval(input())
total = 0.0
for i in range(len(notas)):
	total += notas[i]*pesos[i]
media = total/sum(pesos)
print(round(media,2))