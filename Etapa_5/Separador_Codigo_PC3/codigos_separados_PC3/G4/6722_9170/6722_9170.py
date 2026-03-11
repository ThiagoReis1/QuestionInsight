x = int(input("Valor de X: "))

if x%17 == 0:
	
	imp = "sim"
	a = x//17
else:
	imp = "nao"
	a = x%17
	
print(a)
print(imp)
 