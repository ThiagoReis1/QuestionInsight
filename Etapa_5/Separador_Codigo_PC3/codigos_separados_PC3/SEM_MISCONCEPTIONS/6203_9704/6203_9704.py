alt_leao = float(input(""))
taxa_leao = float(input(""))

alt_mcc = 1.4
tx_mcc = 0.06

ano = 0

while alt_mcc < alt_leao:
	alt_mcc += tx_mcc
	alt_leao += taxa_leao
	ano += 1

print(ano)