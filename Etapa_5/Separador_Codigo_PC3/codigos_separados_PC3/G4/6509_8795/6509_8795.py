h = int(input("horas: "))
p = int(input("quantidade de pratos: "))

if h>=18 :
	f = (p*28.50)
	d = f*(20/100)
	e = (f-d)
	print(round(e, 1))

else :
	t = (p*28.50)
	print(round(t, 1))