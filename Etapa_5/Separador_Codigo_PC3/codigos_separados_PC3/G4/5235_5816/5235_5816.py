n = int(input(""))
if(n % 3 == 0 and n % 5 == 0):
	print("Zuuum")
elif(n % 5 == 0):
	print("Plact")
elif(n % 3 == 0):
	print("Plunct")
else:
	print(n)