from numpy import*

a=input("digite:").lower().upper()
b=len(a)

c_maiuscula=False
c_minuscula=False

for i in range(b):
	if(a[i].islower()==True):
		a[i].upper()
	elif(a[i].isupper()==True):
		a[i].lower()
		

		
print(a)
		
		