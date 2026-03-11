qtd_c = float(input("insira a quantidade de combustivel: "))

if qtd_c < 17.5:
	total = qtd_c + 1.5
elif qtd_c >= 17.5 and qtd_c < 35.0:
	total = qtd_c + 2.3
elif qtd_c >= 35.0 and qtd_c < 50.0:
	total = qtd_c + 3.3
elif qtd_c >= 50.0:
	total = qtd_c + 4.7
print(round(total,2))