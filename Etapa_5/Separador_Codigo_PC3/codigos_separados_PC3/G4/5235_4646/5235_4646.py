n=int(input("numero"))
k=n%3
l=n%5
if(k==0 and l==0):
	print("Zuuum")
elif(k==0):
	print("Plunct")
elif(l==0):
	print("Plact")
else:
	print(n)