var1 = input("Face: ")

a = 0 #ARREMESSO
cara = 0 #CARAS
coroa = 0 #COROA

while (var1.upper() != "S"):
	if var1.upper() == "CARA":
		cara = cara + 1	
	else:
		coroa = coroa + 1
	var1 = input("Face: ")	
a = cara + coroa
p = (cara/a) * 100
print(a)
print(round(p,2))
	
	
	