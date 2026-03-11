# faça seu código aqui!

var1 = float(input("quantos dias foram reservados? "))

if(var1 < 15):
	print(round(((var1 * 175) + 20), 2))
	
elif(var1 == 15):
	print(round(((var1 * 175) + 16), 2))
	
else:
	print(round(((var1 * 175) + 10), 2))