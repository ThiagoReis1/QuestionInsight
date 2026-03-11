item = input("Digite um item ('T' para 'Tapioca' e 'S' para 'Salgado'): ").upper()
quantidade_tapioca_salgado = float(input("Digite a quantidade de tapioca: "))
quantidade_acai = float(input("Digite a quantidade de acai: "))

tapioca = 5.50
salgado = 4.00
acai = 10.00

if (item == 'T'):
	valor_total_tapioca = quantidade_tapioca_salgado * tapioca + quantidade_acai * acai
	print(round(valor_total_tapioca, 2))

elif (item == 'S'):
	valor_total_salgado = quantidade_tapioca_salgado * salgado + quantidade_acai * acai
	print(round(valor_total_salgado, 2))

else:
	print("valores indisponiveis")