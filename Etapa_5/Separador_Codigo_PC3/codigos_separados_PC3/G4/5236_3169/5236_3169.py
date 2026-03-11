n = int(input())
a = n%3
b = n%5

if(n>=0):
	if(a==0 and b==0):
		print("PirlimPimpim")
	elif(a==0):
		print("Pirlim")
	elif(b==0):
		print("Pimpim")
	else:
		print(n)
else:
	print("numero invalido")