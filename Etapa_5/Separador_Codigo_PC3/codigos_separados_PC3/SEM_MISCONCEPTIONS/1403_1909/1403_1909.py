#inicio program
nome_arm = input("digite o nome da armadura:")
fator_dt = int(input("digite o valor de destreza:"))

if(nome_arm == "malha"):
	resistencia = (15 * fator_dt) - 1 
	print(int(resistencia))
else:
	resistencia = (20 * fator_dt) - 18
	print(int(resistencia))