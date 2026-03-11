valora = float(input("valora:"))
valorb = float(input("valorb:"))
valorc = float(input("valorc:"))
limite = float(input("limite:"))

total = valora + valorb + valorc

if (total <= limite):
	print (total)
	print("Nao ultrapassou")

else:

	print(total)
	print("Ultrapassou")