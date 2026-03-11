n = input("").upper()
cont = 1
cara = 0
coroa = 0

while(n!="S"):
	while(n=="CARA"):
		cont = cont + 1
		cara = cara+1
		n = input("").upper()
	while(n=="COROA"):
		cont = cont + 1
		coroa = coroa+1
		n = input("").upper()
print(cara)