x = float(input("preco sem desconto: "))
y = int(input("codigo da regiao de entrega: "))

a = 1
b = 2
c = 3
d = 4

if(y == a):
	v = (x-x*0.4) + x * (10/ 100)
	print(round(v,2))
elif(y == b):
	v = (x-x*0.4) + x * (8/ 100)
	print(round(v,2))
elif(y == c):
	v = (x-x*0.4) + x * (0/ 100)
	print(round(v,2))
elif(y == d):
	v = (x-x*0.4) + x * (2/ 100)
	print(round(v,2))
	
	
	

