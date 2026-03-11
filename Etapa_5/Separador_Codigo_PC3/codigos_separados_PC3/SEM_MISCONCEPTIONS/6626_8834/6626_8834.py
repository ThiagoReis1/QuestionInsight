palavra=(input())
contadora=0
palavra = palavra.upper()
i=0
tamanho= len(palavra)
while i<tamanho:
	if palavra[i]== "C":
		contadora+=1
	i+=1 
	
print(contadora)