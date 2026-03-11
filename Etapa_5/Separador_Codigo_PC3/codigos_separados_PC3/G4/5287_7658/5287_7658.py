m=input("CARA OU COROA").upper()
cont=0
cara = 0
while m != 'S':
	if m == 'CARA':
		cara += 1
	cont += 1
	m=input("CARA OU COROA").upper()
print(cont)
print(round(cara/cont*100,2))