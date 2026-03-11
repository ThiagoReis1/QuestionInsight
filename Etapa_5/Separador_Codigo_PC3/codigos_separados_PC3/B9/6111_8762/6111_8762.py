x = float(input("Informe o valor do combustivel comum: "))

if(x<17.5):
	total = x+10.5
	print(round(total,1))
elif(x>=17.5 and x<35.0):
	total = x+14.0
	print(round(total,1))
elif(x>=35.0 and x<50.0):
	total = x+18.6
	print(round(total,1))
else: 
	total = x+24.5
	print(round(total,1))