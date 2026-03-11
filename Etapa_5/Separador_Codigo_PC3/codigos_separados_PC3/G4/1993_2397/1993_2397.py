n= input().lower()
if(n=="cisteina"):
	p=3*12.011 +7*1.00794 + 1*14.0067 +2*15.9994 +1*32.066
	print(round(p,2))
elif(n=="isoleucina"):
	p=6*12.011 +13*1.00794 + 1*14.0067 +2*15.9994 
	print(round(p,2))
elif(n=="metionina"):
	p=5*12.011 +11*1.00794 + 1*14.0067 +2*15.9994 +1*32.066
	print(round(p,2))
else:
	print("Entrada:",n)
	print("Dado Invalido")