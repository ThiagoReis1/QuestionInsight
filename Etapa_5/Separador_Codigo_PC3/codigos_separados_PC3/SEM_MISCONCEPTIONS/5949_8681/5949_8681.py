nam = input("O que voce deseja? (B/C): ")
qtt = int(input("Insira a quantidade de fatias: "))
qtt2 = int(input("Insira a quantidade de cappuccinos: "))

precoA = 6
precoB = 3
precoC = 5.50

if (nam.upper() == "B"):
	valortotal = (qtt*precoB) + (qtt2*precoC)
else:
	valortotal = (qtt*precoA) + (qtt2*precoC)
	
print(round(valortotal,2))