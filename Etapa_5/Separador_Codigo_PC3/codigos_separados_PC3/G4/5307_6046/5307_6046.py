x= float(input("numero real: "))
k= int(input("numero real: "))

cont= 1
ac= 0

while cont<=k:
	ac= cont/x + ac
	cont= cont +1
	
print(round(ac, 10))