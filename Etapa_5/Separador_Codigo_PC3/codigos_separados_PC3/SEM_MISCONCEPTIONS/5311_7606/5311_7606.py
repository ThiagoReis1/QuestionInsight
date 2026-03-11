d_i = float(input("qual o total do deposito"))
meses = int(input("quantidade de meses"))
i = 0


while (i < meses):
	d_i= d_i + (d_i * (1.2/100))
	i = i + 1
	print(round(d_i, 2))
	
	