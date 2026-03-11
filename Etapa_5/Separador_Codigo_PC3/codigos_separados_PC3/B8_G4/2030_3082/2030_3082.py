r = input("resultado do primeiro: ")
Q = 0
q = 0
while(r != "S"):
	if(r == "CARA"):
		q = q+1
	elif(r == "COROA"):
		Q = Q+0
	r = input("proximo: ")
print(q)