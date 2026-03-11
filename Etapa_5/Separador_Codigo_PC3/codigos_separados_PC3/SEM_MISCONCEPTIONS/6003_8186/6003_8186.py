quantidade = int(input("quantidade de cenouras: "))

if quantidade < 5:
	print(round(quantidade*1.20, 2))
	
else:
	print(round(quantidade*0.90, 2))