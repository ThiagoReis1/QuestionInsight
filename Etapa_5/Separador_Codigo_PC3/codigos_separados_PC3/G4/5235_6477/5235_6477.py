N = int(input("N: "))
if (N%3==0 and not(N%5==0)):
	print("Plunct")
elif(N%5==0 and not (N%3==0)):
	print("Plact")
elif(N%3==0 and N%5==0):
	print("Zuuum")
else:
	print(N)