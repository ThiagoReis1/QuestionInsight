from numpy import*
senha = input("digite a senha: ").upper()
custo = 0
for caractere in senha: 
	if caractere in "AEIOU":
		
		custo += 3.15
	else:
		custo += 4.17
print(round(custo,2))

	

