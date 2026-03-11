p = float(input("preco: "))
c = int(input("codigo: "))

if(c==1):
	v = p-(p * 0.40) + (p * 0.10)
	print(round(v,2))
	
elif(c==2):
	v = p-(p * 0.40) + (p * 0.08)
	print(round(v,2))
	
elif(c==3):
	v = p-(p * 0.40)
	print(round(v,2))
	
elif(c==4):
	v = p-(p * 0.40) + (p * 0.02)
	print(round(v,2))
	