cenouras = int(input("digite a quantidade de cenouras:"))

if cenouras < 5:
	print(round( cenouras * 1.20, 2))

else:
	print(round(cenouras * 0.90, 2))