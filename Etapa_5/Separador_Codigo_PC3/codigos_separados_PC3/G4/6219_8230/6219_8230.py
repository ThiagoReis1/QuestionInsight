x = int(input("informe um valor para x: "))
y = int(input("informe um valor para y: "))

num = x
cont = 0

while(num >= x and num <= y):
	if(num % 3 == 0):
		cont = num + cont
	
	else:
		print(cont)