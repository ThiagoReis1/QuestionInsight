n = int(input("inteiro poitivo: "))
i = 0
a = 0
while(n != 0):
	if(n > 0):
		i = i + 1
	if(n % 3 == 0):
		 a = a + 1
	n = int(input("inteiro positivo: "))
	
x = (a/i)*100
print(i)
print(round(x,2))