a = input("digite o dia de semana: ")
b = int(input("quantidade de pratos: "))
c = 22
desconto = 0.15
if(a == "qua"):
	z = b*c-b*c*desconto
	print(round(z,2))
	
else:
	d = b*c
	print(round(d,2))