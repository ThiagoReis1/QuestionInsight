vl = float(input("valor total da compra:"))
cp = input("codigo da compra:")
if cp == "D":
	soma1= vl- (0.17*vl)
	print(round(soma1,2))
elif cp == "p":
	soma2= vl - (0.17*vl) 
	print(round(soma2,2))
elif cp == "C1":
	print(vl)
elif cp == "C2":
	soma3= (0.08*vl)+vl
	print(round(soma3,2))
	