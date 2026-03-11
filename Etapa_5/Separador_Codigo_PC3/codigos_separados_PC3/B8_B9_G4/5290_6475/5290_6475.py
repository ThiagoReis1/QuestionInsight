num= int(input('dados lancados: '))
quant= 0
num5= 0

while(num!=-1):
	if (num==5):
		num5= num5+1
		quant= quant+1
	elif ((num>=1) and (num<=10) and (num!=5)):
		quant= quant+1
		num5= num5+0
	num= int(input('dados lancados: '))
	
eq= (num5*100)/quant

print(quant)
print(round(eq, 2))