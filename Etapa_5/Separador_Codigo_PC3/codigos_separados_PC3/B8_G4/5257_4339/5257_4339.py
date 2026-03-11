p= float(input("Preco de custo:"))

if(p <= 50.0):
	vf= p * 2
	print(round(vf,2))
elif(p >= 50.01) and (p <= 100.0):
	vf= (p * 0.50) + p
	print(round(vf,2))
elif(p >= 100.01) and (p <= 500.00):
	vf= (p * 0.40) + p
	print(round(vf,2))
elif(p > 500.00 ):
	vf= (p * 0.30) + p
	print(round(vf,2))
	