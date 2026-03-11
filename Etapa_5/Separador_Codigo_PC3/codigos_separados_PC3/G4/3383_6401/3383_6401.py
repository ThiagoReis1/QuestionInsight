m = input("K para quilos, L para libras: ")
p = float(input("Qual o peso: "))

if(m == "K"):
	var1 = 2.20462 * p
	
else:
	var1 = p / 2.20462
	
print(round(var1, 2))