x = int(input("valor x: "))
y = int(input("valor y: "))
cont = 0
num = x
while num <= y:
	if num % 3 == 0:
		cont = cont + num
	num  = num + 1
print(cont)
