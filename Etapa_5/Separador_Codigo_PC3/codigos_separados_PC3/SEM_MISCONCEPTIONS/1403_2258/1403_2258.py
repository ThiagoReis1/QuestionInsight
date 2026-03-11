nome = input("Digite o nome da armadura(malha/placas): ")
fator = int(input("Digite um valor entre 1 e 8: "))

if(nome=="malha"):
	resistencia = (15 * fator) - 1
	
else:
	resistencia = (20 * fator) - 18

print(resistencia)