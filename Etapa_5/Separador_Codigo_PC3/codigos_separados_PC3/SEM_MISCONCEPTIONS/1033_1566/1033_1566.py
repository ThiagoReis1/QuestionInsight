#Ronilson de Souza Bezerra

valor = float(input("quantos quilos voce quer despachar?: "))

custo = (valor * 43.21) + 25.00

imposto = (custo * 62) / 100

total = custo + imposto

print(round(total, 2))