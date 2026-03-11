arma = input("Digite nome da arma: ")
destreza = float(input("Digite a destreza: "))
dados1 = int(input("Digite o valor sorteado:(D1/D2) "))
dados2 = int(input("Digite o valor sorteado:(D1/D2) "))
S = dados1 + dados2
katana = (2 * S) + destreza
sabre = (S + 2*destreza)

if (arma == "katana"):
	msg = katana
else:
	msg = sabre

print(msg)