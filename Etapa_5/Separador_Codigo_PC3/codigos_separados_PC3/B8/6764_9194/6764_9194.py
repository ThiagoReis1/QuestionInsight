peso= float(input('inserir o peso do pacote:'))

if peso<5:
	total= 10+3.75
elif peso==5:
	total= 10+4.75
elif peso>5:
	total= 10+5.75
print(round(total,2))