# faça seu código aqui!
combo = int(input("Digite a quantidade de manhas energeticas do cliente:"))
valorcombo = 20.00 * combo 
if combo >= 4:
	desconto= valorcombo * 15/100
	valor= valorcombo - desconto
	print(round(valor,2))

else:
	print(round(valorcombo,2))
