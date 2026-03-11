dias = int(input("qnt de dias:"))

if (dias < 7 ):
   tt = dias * 100 + 15.00
elif (dias == 7 ):
	tt = dias * 100 + 12.00
elif (dias > 7 ):
   tt = dias * 100 + 10.00

	
print(round(tt, 2))


	