giro = input(":").upper()
n = 0
p=0

while giro!="S":
	if giro == "PRETA":
		p = p+1
		n = n+1
		giro = input("E").upper()
	else: 
		n=n+1
		giro = input("A").upper()
	
print(n)
pp= p*100/n
print(round(pp,2))
	
	
		

		 