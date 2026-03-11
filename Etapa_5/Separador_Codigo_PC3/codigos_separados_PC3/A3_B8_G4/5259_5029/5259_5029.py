m = float(input("Valor da mensalidade: "))
n = int(input("Numero de criancas da familia: "))

if (n == 1) :
	x = (m*10)/100
	y = m-x
	z = y*n
	z = round(y,2)
	print(z)
elif (n == 2) :
	x = (m*30)/100
	y = m-x
	z = y*n
	z = round(z,2)
	print(z)
elif (n >= 3) :
	x = (m*40)/100
	y = m-x
	z = y*n
	z = round(z,2)
	print(z)