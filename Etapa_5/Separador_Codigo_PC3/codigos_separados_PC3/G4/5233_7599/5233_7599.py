n = int(input("numero:"))
x = n%3
y = n%5
if(1<=n):
	if((x==0) and (y==0)):
		print("AuauMiau")
	else:
		if(x==0):
		   print("Auau")
		else:
			if(y==0):
				print("Miau")
			else:
				print(n)
	