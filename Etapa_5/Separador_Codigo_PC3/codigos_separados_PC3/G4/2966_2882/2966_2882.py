sn=input(" ")
preco=float(input(" "))
q=int(input(" "))

if(sn=='S'):
	vt=(preco*q)*0.8
	print(round(vt,2))

else:
	vt=preco*q
	print(round(vt,2))