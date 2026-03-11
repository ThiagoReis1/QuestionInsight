aboboras_compradas = float(input("Digite a quantidade: "))
if ( aboboras_compradas < 5) :
   valor_total = aboboras_compradas * 3.80
   print(round(valor_total, 2))
else:
	valor_total = aboboras_compradas * 3.45
	print(round(valor_total, 2))