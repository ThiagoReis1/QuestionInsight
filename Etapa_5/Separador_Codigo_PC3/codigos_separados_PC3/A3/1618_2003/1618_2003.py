from numpy import *

termos = array(eval(input("Termos: ")))
i = 0
k = 1
saida = ""
termo = str(termos)
while i < size(termos):
	saida = saida + termos[i]
	
	i = i + 1
	k = k - 1

print(saida)
print(termos)
print(termos[0])