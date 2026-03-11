num = int(input("num:"))
cont = 0
if num>=101 and num<=201:
	cont = 1
while num != -1:
	num = int(input("num:"))
	if num >=101 and num<=201:
		cont += 1
print(cont)