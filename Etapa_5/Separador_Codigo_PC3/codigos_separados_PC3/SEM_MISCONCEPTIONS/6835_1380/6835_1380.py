from numpy import *

s = input("Informe a sequencia de identificadores de produtos: ")
precos = [3.75, 7.90, 9.85]
ids = ["B", "C", "E"]

valor_total = 0
i = 0
while (i < len(s)):
	
	j = 0
	while (j < size(ids)):
		if (ids[j] == s[i]):
			valor_total += precos[j]
			j = size(ids) # para finalizar a busca
		
		j += 1
	
	i += 1
	
print(round(valor_total, 2))