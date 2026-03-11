x = int(input())
cont = 0

while x > 0:
	if x>=35 and x <=95:
		cont = cont + 1
		x = int(input())
	else:
		x = int(input())
print(cont)