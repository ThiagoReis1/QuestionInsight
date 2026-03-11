num=input("cara ou coroa: ").upper()
quant=0
caras=0

while(num!='S'):
	if(num=='CARA'):
		caras=caras+1
		quant=quant+1
	elif(num=='COROA'):
		quant=quant+1
	num=input("cara ou coroa: ").upper()
eq=(caras*100)/quant
print(quant)
print(round(eq, 2))