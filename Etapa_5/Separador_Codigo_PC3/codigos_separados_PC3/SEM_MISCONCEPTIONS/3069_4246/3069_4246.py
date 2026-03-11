nome = str(input())
a = int(input())
b = int(input())

if((nome == "FURIA") and ((a + b => 1) and (a + b <= 8))):
	x = a + b + 10
	print(x)
elif((nome == "GRITO") and ((a + b => 1) and (a + b <= 8))):
	x = a + b + 6
	print(x)
elif(nome == "TOQUE") and ((a+b=>1) and (a+b<=8)):
	print((a + b)**2)
else:
	print("Entrada invalida")