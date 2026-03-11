x = int(input("valor de X  "))
y = int(input("valor de Y  "))
cont = x
while cont<=y:
	par = cont%2

	if par==0:
		print(cont)
	cont +=1