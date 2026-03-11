limit = float(input("valor do limite:"))
c1 = float(input("valor da compra: "))
c2 = float(input("valor da compra: "))
c3 = float(input("valor da compra: "))
c4 = float(input("valor da compra: "))

soma = c1 + c2 +c3 +c4
if(soma <= limit):
	print(round(soma, 2))
	msg = "Dentro do limite"

else:
	print(round(soma, 2))
	msg = "Estourou o limite"

print(msg)