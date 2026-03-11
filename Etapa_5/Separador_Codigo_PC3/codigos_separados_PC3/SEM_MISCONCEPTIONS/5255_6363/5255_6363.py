
p = float(input("peso: "))
d = float(input("distancia: "))
c = int(input("codigo: "))
custokg = p*25.00
custokm = d*0.10
if(c==1):
	total = (custokg + custokm) * (1 + (17.0/100))
	print(round(total, 2))
elif(c==2):
	total = (custokg + custokm) * (1 + (17.5/100))
	print(round(total, 2))
elif(c==3):
	total = (custokg + custokm) * (1 + (18.0/100))
	print(round(total, 2))
else:
	total = (custokg + custokm) * (1 + (20.0/100))
	print(round(total, 2))





