prato= int(input(" : "))
sobremesa= int(input(" : "))
bebida= int(input(" : "))
c=0
a=0
l=0
if prato <1 or prato> 4 or sobremesa < 1 or sobremesa > 4 or bebida <1 or bebida >4:
	print("Dados invalidos")
else:
	if prato == 1:
		c= 180
	if sobremesa == 1:
		a= 75 
	if bebida == 1:
		l= 20
	if prato == 2:
		c= 230
	if sobremesa == 2:
		a= 110
	if bebida == 2:
		l= 70
	if prato == 3:
		c= 250
	if sobremesa == 3:
		a= 170
	if bebida == 3:
		l= 100
	if prato == 4:
		c= 350
	if sobremesa == 4:
		a= 200
	if bebida == 4 :
		l= 65 
	soma = c + a + l
	total= print("Calorias:", soma, "cal") 



