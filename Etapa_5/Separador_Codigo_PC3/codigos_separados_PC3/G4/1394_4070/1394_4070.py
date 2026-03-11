q = float(input("Quantidade de horas:"))


if (q<=20):
	msg= q*50
	print(round(msg,2))
else :
	msg= 20*50 + (q-20)*70
	print(round(msg,2))