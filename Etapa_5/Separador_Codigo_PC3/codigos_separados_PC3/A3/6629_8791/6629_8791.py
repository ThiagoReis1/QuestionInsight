frase =(input())
frase = frase.upper()
contador_e = 0
i = 0
tamanho = len(frase)
while i < tamanho:
	if frase[i]==("P"):
		print(i)
	i+=1
if "P"not in frase:
	print("nao achei")
