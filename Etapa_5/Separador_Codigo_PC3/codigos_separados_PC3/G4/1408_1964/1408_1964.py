arma = input("Digite o tipo de arma: ")
D = float(input("Destreza do personagem: "))
D1 = float(input("Valor do dado 1 de 10 faces: "))
D2 = float(input("Valor do dado 2 de 10 faces: "))
S = D1+D2

if(arma =="katana"):
	print(2*S + D)
else:
	print(S+2*D)
