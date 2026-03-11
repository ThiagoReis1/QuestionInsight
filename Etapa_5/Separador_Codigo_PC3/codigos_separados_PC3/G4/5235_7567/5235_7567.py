#N >= 1 
N = int(input(""))
if((N%3 == 0) and (N%5 == 0)):
	print("Zuuum")
elif(N%3 == 0):
	print("Plunct")
elif(N%5 == 0):
	print("Plact")
else:
	print(N)