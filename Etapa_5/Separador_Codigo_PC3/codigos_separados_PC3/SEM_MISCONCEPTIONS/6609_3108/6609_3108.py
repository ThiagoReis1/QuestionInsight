integer = int(input())
while(integer <= 0):
	if(integer % 3 == 0):
		print(integer)
		integer = integer + 3
	else:
		integer = integer + 1
print("fim")