patrimonio_podresco = float(input("Entre com o patrimonio atual do Podresco: "))

patrimonio_bitcoin = float(input("Entre com o patrimonio atual do Bitcoin: "))

percentual_podresco = float(input("Entre com o percentual de crescimento do Podresco: "))

percentual_bitcoin = float(input("Entre com o percentual de crescimento do Bitcoin: "))

ano = 1

while ( patrimonio_bitcoin <= patrimonio_podresco):
	patrimonio_podresco = patrimonio_podresco + percentual_podresco * patrimonio_podresco / 100
	patrimonio_bitcoin = patrimonio_bitcoin + percentual_bitcoin * patrimonio_bitcoin / 100
	ano = ano + 1
print(ano)
	