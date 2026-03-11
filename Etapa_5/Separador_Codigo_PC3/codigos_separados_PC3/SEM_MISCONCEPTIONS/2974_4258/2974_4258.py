q_acai = int(input("Quantidade de acai no copo em gramas: "))
q_salg = int(input("Quantidade de salgados: "))
pag = float(input("Valor pago em dinheiro: "))

valor_tot = q_acai*0.001*24 + q_salg*3
print(round(valor_tot, 2))

if(pag > valor_tot):
	print("Sim")

else:
	print("Nao")