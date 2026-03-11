bc = input("o quevai ser?: ").upper()
quantbc = int(input("quantidade de fatias: "))
quantc = int(input("quantidade de cappuccinos: "))

if bc == "B":
	conta = (quantbc*3) + (quantc*5.50)
	print(round(conta, 1))
	
else:
	conta = (quantbc*6) + (quantc*5.50)
	print(round(conta, 1))