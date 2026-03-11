num = input("entre como cara ou coroa: ").upper()
ca = 0
co = 0
while (num!= "S"):
	if(num =="CARA"):
		ca = ca + 1
	
	num = input("entre como cara ou coroa: ").upper()
	
print(ca)