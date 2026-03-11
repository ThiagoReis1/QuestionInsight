H==float(input("numero de horas extras:"))
h==float(input("numero de horas nao trabalhadas"))
H==h*2/3

if (H<0 or h<0):
	print("Entradas:", H, ",", h)
	print("Dados invalidos")
elif (H>2400.00):
		Gratificacao=500.00
		print("Entradas:", H,"horas extras e", "Gratificacao: R$")
	elif (H>1800.00 and H<2400.00):
		Gratificacao=400.00
		print("Entradas:", H,"horas extras e", "Gratificacao: R$")
	elif (H>1200.00 and H<1800.00):
		Gratificacao=300.00
		print("Entradas:", H,"horas extras e", "Gratificacao: R$")
	elif (H>600.00 and H<1200.00):
		gratificacao=200.00
		print("Entradas:", H,"horas extras e", "Gratificacao: R$")
	elif (H<600.00):
		Gratificacao=100.00
		print("Entradas:", H,"horas extras e", "Gratificacao: R$")
else:
	print("Dados invalidos")
			
	

