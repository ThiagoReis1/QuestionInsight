s= float(input("salario atual: "))

if(s<1212):
	n=s+s*12/100
	print(round(n, 2))
elif(1212<=s<=5000):
	n=s+s*8/100
	print(round(n, 2))
elif(s>5000):
	n=s+s*3/100
	print(round(n, 2))
else:
	print("")
	
