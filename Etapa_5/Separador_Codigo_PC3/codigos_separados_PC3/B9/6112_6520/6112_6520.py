combustivel=int(input("combustivel disponivel: "))

if combustivel < 17.5:
	mistura=combustivel + 10.5
elif combustivel >= 17.5 and combustivel < 35:
	mistura=combustivel + 14
elif combustivel >= 35 and combustivel < 50:
	mistura = combustivel + 18.6
else:
	mistura = combustivel + 24.5
print(round(mistura,1))