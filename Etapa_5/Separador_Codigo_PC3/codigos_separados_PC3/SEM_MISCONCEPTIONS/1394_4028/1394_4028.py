q=int(input("quantidade de horas:"))
if(q == 20):
	pagamento=50*q
else:
	pagamento=50*q + 70*q
print(round(pagamento,2))