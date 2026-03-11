dados = eval(input('dados:'))
i = 0
for dado in dados:
	if dado == 1:
		i += 10
	elif dado == 2 or dado == 4:
		i += 5
	elif dado == 5:
		i += 20
	elif dado == 6:
		i += 10
print(i)