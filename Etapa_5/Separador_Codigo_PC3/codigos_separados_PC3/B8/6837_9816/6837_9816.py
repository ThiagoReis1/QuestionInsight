comida = input("Digite a comida que voce quer:").upper()

i = 0
cont = 0

while i<len(comida):
	if comida[i]=='I':
		cont+=3.75
	elif comida[i]=='M':
		cont+=4.50
	elif comida[i]=='S':
		cont+=2.90
	i+=1
print(round(cont,2))
	