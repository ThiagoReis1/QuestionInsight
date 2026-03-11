x = float(input("preco de custo:"))

if(x<=50):
	print(round(x + x,2))
elif(50.1<=x<=100):
	print(round(x + x*0.5,2))
elif(100.1<=x<=500):
	print(round(x + x*0.4,2))
else:
	print(round(x + x*0.3,2))


