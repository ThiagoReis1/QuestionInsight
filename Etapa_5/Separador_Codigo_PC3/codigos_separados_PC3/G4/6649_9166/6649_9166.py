peso = [3, 2, 4, 1, 3]
nota = list(eval(input()))

i, soma = 0, 0
while (i < len(nota)):
	soma = soma + nota[i] * peso[i]
	i = i + 1
	
media = soma / sum(peso)
print(round(media, 2))