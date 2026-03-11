peso =float(input("peso da encomenda: "))

a =peso * 0.04 + 60 
 
b = peso * 0.05

if(peso >= 5000.0):
	print(round(a ,2))
else:
	print(round(b , 2))