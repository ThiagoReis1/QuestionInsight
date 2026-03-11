


rotulo = input("")

rotulo.upper

custo = 0 

for letra in rotulo.upper():
	if letra in "AEIOU":
		custo += 0.12
	else :
		custo +=0.18
		
custototal= round(custo,2)

print("",custototal)