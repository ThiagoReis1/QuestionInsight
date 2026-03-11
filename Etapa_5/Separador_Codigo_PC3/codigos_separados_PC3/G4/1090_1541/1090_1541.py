a= float(input("digite o valor da compra"))
b= float(input("digite o valor da compra"))
c= float(input("digite o valor da compra"))
d= float(input("digite o valor da compra"))
l= float(input("digite o valor do limite"))

total=a+b+c+d

if(total<=l):
	print(round(total,2))
	print("Sim")
else:
	print(round(total,2))
	print("Nao")
