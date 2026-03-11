b= int(input("quantidade de pratos: "))
c= 50
desconto = 0.88

if(b>4):
	x=(b*c*desconto)
	print(round(x,2))
else:
	y = (b*c)
	print(round(y,2))