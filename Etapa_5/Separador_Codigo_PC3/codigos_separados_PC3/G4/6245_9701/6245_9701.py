aval = input("digite S, I, N ").upper()
cont = 0
while aval != "X":
	if aval == "S":
		cont += 1
	aval = input("digite S, I, N ").upper()
		
print(cont)