from numpy import*
a = input("Digite algo :")
x = len(a)

c_minuscula=False
c_maiuscula=False

for i in range(x):
	if(a[i].islower()==True):
		a[i].upper()
	elif(a[i].isupper()==True):
		a[i].lower()

print(a)


	
