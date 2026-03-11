combustivel= float(input("Digite a quantidade de combustivel: "))

if combustivel<17.5:
	total= combustivel+0.8
	print(round(total,1))
elif 17.50<combustivel<35.0:
	total= combustivel+1.3
	print(round(total,1))
elif 35.0<combustivel<50.0:
	total= combustivel+ 2.1
	print(round(total,1))
else:
	total= combustivel+ 3.0
	print(round(total,1))


