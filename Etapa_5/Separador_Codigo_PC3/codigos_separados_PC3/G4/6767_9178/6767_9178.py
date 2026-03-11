v = float(input("Valor total da caompra: "))
c = input("Codigo do pagamento: ")

d1 = v - (v*(12/100))
p1 = v - (v*(12/100))
c11 = v
c21 = v + (v*(7/100))

if(c == "D"):
	print(round(d1,2))
	
elif(c == "P"):
	print(round(p1,2))
	
elif(c == "C1"):
	print(round(c11,2))
	
elif(c == "C2"):
	print(round(c21,2))
	
else:
	print("ERRO")


