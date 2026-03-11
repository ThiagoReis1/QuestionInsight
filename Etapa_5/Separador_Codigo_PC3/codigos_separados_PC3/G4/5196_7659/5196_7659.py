produtos = float(input("digite o valor: "))

p1 = (produtos * 5)/100
p2 = (produtos * 15)/100
p3 = (produtos + p1)
p4 = (produtos + p2)

if(produtos>100.00):
	msg = p4
	msg1 = "Aumento de 15 porcento"
else:
	msg = p3
	msg1 = "Aumento de 5 porcento"


print(round(msg, 2),"ryous")

print (msg1)
	
