valor_consumido=float(input(""))
desconto1= (valor_consumido*10)/100

desconto2=(valor_consumido*6)/100

if (valor_consumido<=300.00):
	print(round(valor_consumido+desconto1, 2 ))

else:
	print(round(valor_consumido+desconto2, 2))
