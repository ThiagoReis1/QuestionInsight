n=int(input("numero:"))
m3=0
imp=0
cont=0
while(n!=0):
	if(n%3==0):
		m3=m3+1
	n=int(input("numero:"))
	cont=cont+1

por=m3*100/cont
print(cont)
print(round(por,2))
	
	