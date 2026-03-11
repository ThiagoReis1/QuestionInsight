# faça seu código aqui!
dia = int(input("Qual a quantidade de dias de reservas? "))
c1 = (dia * 175.00) + 20.00
c2 = (dia * 175.00) + 16.00
c3 = (dia * 175.00) + 10.00
if(dia < 15):
	c = c1
	print(round(c, 2))
elif(dia == 15):
	c = c2
	print(round(c, 2))
elif(dia > 15):
	c = c3
	print(round(c, 2))