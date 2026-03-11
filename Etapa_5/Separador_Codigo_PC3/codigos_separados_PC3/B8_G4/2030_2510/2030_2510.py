x = input("Cara ou Coroa: ")
a=0
if x != "S":
	print(a)
elif x == "COROA" or x == "CARA":
	x = input("Cara ou Coroa: ")
	while x == "CARA":
		x = input("Cara ou Coroa: ")
		a+=1
	print(a)