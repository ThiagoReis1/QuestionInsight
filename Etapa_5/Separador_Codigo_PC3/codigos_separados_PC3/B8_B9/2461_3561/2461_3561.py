preco=float(input("preco:"))
if(preco<=50.00):
   print(round(preco+(preco*(100/100)),2))
elif(preco>50.00 and preco<=100):
	print(round(preco+(preco*(50/100)),2))
elif(preco>100 and preco<=500):
	print(round(preco+(preco*(40/100)),2))
elif(preco>500 ):
	print(round(preco+(preco*(30/100)),2))