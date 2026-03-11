m = input().upper()
coroa =0
cara = 0
cont = 0

while(m!="S") :

	cont+=1
	
	if(m=="CARA"):
		cara = cara + 1
	else:
		coroa = coroa +1
	
	m = input().upper()
print(cont)
print(round(cara/cont*100,2))