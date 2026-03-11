frase = input()
frase = frase.upper()
i= 0
tamanho = len(frase)
cont = 0
while i< tamanho:
	if frase[i]=="B":
		cont += 1
	i= i +1
if "B" not in frase:
	print("nao achei")
print
		
