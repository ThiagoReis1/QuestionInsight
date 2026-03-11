x = int(input("Entrada: "))

x1 = 50 + 5.50
x2 = 50 + 7.75
x3 = 50 + 10.00

if(x < 10):
	print(x1)
	
elif(x == 10):
	print(x2)
	
elif(x > 10):
	print(x3)
	
else:
	print("ERRO")