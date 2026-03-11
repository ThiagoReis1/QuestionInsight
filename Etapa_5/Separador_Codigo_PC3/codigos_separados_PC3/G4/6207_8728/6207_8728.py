n= int (input("numero: "))
a = 0
while n != -1:
	if n >=26 and n <= 50:
		a += 1
	n = int(input("numero: "))
print(a)