n=int(input("inteiro: "))
if(n%3==0 and n%5==0):
	print("AuauMiau")
elif(n %5==0):
	print("Miau")
elif(n%3==0):
	print("Auau")
else:
	print(n)