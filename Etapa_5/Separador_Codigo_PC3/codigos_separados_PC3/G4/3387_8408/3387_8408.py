m_k = input("M/K? ")
valor = float(input("valor da medida? "))

if (m_k == "K"):
	mg = 2.35215*valor
	print(round(mg,2))

else:
	k= (valor/2.35215)
	print(round(k,2))