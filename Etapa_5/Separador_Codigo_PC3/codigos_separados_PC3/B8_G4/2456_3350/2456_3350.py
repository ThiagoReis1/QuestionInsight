
v = int(input("Valor da mensalidade"))
n = int(input("Numero de garotitos"))
vt1 = (v*n)*0.9
vt2 = (v*n)*0.7
vt3 = (v*n)*0.6
if(n == 1):
	print(round(vt1,2))
elif(n == 2):
	print(round(vt2,2))
elif(n >= 3):
	print(round(vt3,2))

	