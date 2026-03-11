permanencia_veiculo = float(input("digite as horas de permanencia: "))
tarifa_fixa = 5.00

if(permanencia_veiculo < 2):
	valor_total = tarifa_fixa + 1.25
elif(permanencia_veiculo == 2):
	valor_total = tarifa_fixa + 2.25
else:
	valor_total = tarifa_fixa + 3.25

print(round(valor_total, 2))