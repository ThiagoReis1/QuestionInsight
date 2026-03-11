# MARIA LUÍSA SERRÃO, 05/07/2022

# LEITURA DAS INFORMAÇÕES
consumo = float(input("Qual foi o valor consumido?"))

# CÁLCULO
total_1 = consumo + consumo*0.10
total_2 = consumo + consumo*0.06

# SAÍDA
if consumo <= 300:
	print (round(total_1,2))
else:
	print(round(total_2,2))