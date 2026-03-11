from numpy import array 
valor = eval(input())
maior = 0
final = []
for i in range(len(valor)):
	if valor[i] >= 2000:
		final.append(i)
		maior += 1
final = array(final)
print(maior)
print(final)