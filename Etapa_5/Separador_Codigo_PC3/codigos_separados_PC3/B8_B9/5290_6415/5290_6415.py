faces = int(input("Digite as 10 de faces:"))
result = 0
quant = 0
while(faces != -1):
	if(faces == 5):
		result = result + 1
		quant = quant + 1
	elif((faces >=1) and (faces <= 10) and (faces != 5)):
		quant = quant + 1
		result += 0
	faces = int(input("digite:"))
	
esq = (result * 100) / quant

print(quant)
print(round(esq,2))
	