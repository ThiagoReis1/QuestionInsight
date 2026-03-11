comida = input("B ou S: ")
qf = int(input("quantidades de fatias: "))
qc = int(input("quantidade de cappuccinos; "))

if(comida == "B"):
	total = qf*5.00+qc*7.50
	print(round(total,2))
else:
	total = qf*4.00+qc*7.50
	print(round(total,2))
   