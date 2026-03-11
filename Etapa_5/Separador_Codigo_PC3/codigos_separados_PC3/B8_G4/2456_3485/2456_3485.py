men = float(input("Valor mensalidade em R$: "))
cri = float(input("Quantidade criancas: "))

if(cri == 1):
	x = (men*0.1)
	y = men - x
	print(round(y, 2))
elif(cri == 2):
	s = men*2
	x = s*0.3
	y = s - x
	print(round(y, 2))
elif(cri >= 3):
	s = men*3
	x = s*0.4
	y = s - x
	print(round(y, 2))

