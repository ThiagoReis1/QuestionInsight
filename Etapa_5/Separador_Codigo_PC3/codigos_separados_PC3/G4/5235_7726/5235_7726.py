N = int(input("N:"))
r = N % 3
q = N % 5
if(r==0) and (q==0):
	print("Zuuum")
elif(r==0):
	print("Plunct")
elif(q==0):
	print("Plact")
else:
	print(N)
	