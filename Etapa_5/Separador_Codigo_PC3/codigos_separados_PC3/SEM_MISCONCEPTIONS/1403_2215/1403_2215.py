A = input("nome armadura:")
D = int(input("fator destreza:"))

malha = (15*D)-1
placas = (20*D)-18

if(A.lower() == "malha"):
	resistencia = malha
	
else:
	resistencia = placas

print(resistencia)