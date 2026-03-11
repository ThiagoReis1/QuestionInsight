from numpy import*
x = input("")
a = 0
if (len(x) > 11):
	print("INVALIDO")
for i in range(len(x)):
	if (x[i] % 2 == 0):
		a = a + 1
	print(x - a)
	
		
		
