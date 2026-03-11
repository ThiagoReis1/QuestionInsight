x = input("Escreva seu pedido: ").upper()
i = 0
total = 0

D = 2.25
a = 0

S = 4
b = 0

I = 6.90
c = 0
#cont = 1

while i < len(x):
	if x[i] == "D":
		total += 2.25
		a +=1
	elif x[i] == "S":
		total += 4
		b += 1
	elif x[i] == "I":
		total += 6.90
		c += 1
	i += 1
print(round(total, 2), a, b, c)
	
	
	




