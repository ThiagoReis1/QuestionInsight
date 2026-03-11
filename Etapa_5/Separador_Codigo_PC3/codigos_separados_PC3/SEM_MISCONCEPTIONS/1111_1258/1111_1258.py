horas_faltas = float(input("digite as Horas:"))
horas_extras = float(input("digite as Horas"))
h= ((horas_extras) - 2/3 * (horas_faltas))
if(h>2400):
	print("Entradas: 10.5 horas extras e 2.0 horas de falta")
	print("Gratificação: R$ 500.00")
elif(h>1800<=2400):
	print("Entradas: 10.5 horas extras e 2.0 horas defalta")
	print("Gratificação: R$ 400.00")
elif(h>1200<=1800):
	print("Entradas: 10.5 horas extras e 2.0 horas defalta")
	print("Gratificação: R$ 300.00")
elif(h>600<=1200):
	print("Entradas: 10.5 horas extras e 2.0 horas defalta")
	print("Gratificação: R$ 200.00")
elif(h<=600):
	print("Entradas: 10.5 horas extras e 2.0 horas de falta")
	print("Gratificacao: R$ 100.00")
else:
	print("Entradas: 10.5 horas extras e 2.0 horas de falta")
	print("invalida")
	
	
