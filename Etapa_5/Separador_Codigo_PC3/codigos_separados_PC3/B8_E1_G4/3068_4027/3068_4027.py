nome=input("Nome da arma:")
d=int(input("Destreza: "))
v1=int(input("Primeiro valor sorteado:"))
v2=int(input("Segundo valor sorteado: "))
s = v1 + v2
if((nome == "CIMITARRA" or nome == "KATANA" or nome == "SABRE") and d >= 0 and v1 > 0 and v1 <= 10 and v2 > 0 and v1 <= 10):
	if(nome == "CIMITARRA"):
		dano = 2*s + 2*d
	elif(nome == "KATANA"):
		dano == 2*s + d
	elif(nome == "SABRE"):
		dano = s + 2*d
	print(dano)
else:
	print("Entrada invalida")