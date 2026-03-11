dias = int(input())

if dias < 7:
	a_pagar = dias * 100 + 15
else:
	if dias == 7:
		a_pagar = dias * 100 + 12
	else:
		a_pagar = dias * 100 + 10

print(round(a_pagar,2))
