v = float(input("Determine o valor: "))
pag = input('Determine a forma de pagamento: ').upper()

if pag == 'C':
	parc = int(input('Escolha 1 ou 2 parcelas: '))
	if parc == 1:
		t = round(v + 0 , 2)
	elif parc == 2:
		t = round(v + v * 0.07 , 2)
elif pag == 'D':
	t = round(v * 0.88 , 2)
elif pag == 'P':
	t = round(v * 0.88 , 2)

print(t)