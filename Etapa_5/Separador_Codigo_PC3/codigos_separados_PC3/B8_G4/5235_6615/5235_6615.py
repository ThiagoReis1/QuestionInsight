N= int(input("digite um numero: "))
if(N%3==0 and N%5==0):
	print("Zuuum")
else:
	if(N%5==0):
		print("Plact")
	elif(N%3==0):
		print("Plunct")
	elif(N%3!=0 and N%5!=0):
		print(N)