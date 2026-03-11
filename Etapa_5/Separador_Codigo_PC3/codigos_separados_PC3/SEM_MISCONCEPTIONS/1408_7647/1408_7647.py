nome_da_arma = str(input("Insira o nome da arma: "))
destreza = float(input("Insira a sua Destreza: "))
D1 = float(input("Insira o primeiro dado: "))
D2 = float(input("Insira o seguno dado: "))

S = D1+D2

katana = str("katana")
sabre = str("sabre")

if(nome_da_arma == katana):
	dano = 2 * S + destreza
	print(dano)
	
if(nome_da_arma == sabre):
	dano = S + 2*destreza
	print(dano)