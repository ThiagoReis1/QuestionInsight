n=int(input())

if(n>=1):
	if(n%3==0 and n%5!=0):
		print("Pirlim")
	elif(n%5==0 and n%3!=0):
		print("Pimpim")
	elif(n%3==0 and n%5==0):
		print("PirlimPimpim")
	elif(n%3!=0 and n%5!=0):
		print(n)