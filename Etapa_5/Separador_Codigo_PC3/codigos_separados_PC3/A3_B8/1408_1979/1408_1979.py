arma = input("Insira o nome da arma escolhida:\n")
destreza = int(input("Informe a destreza do personagem:\n"))
valor1 = float(input("Insira o primeiro valor sorteado:\n"))
valor2 = float(input("Insira o segundo valor sorteado:\n"))
dano = 0
soma = valor1 + valor2

if(arma == "katana"):
	dano = 2 * soma + destreza
else:
	if(arma == "sabre"):
		dano = soma + 2 * destreza

print(dano)