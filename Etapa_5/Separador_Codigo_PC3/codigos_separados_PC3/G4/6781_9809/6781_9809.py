d = int(input())
p = input().upper()
pp = 2023 - d
if (pp>=21 and p=="B"):
	print("sim")
	pp -= 21
	print(pp)
elif (pp<21 and p=="B"):
	pp -= 21
	pp *= -1
	print("nao")
	print(pp)
elif (pp>=18 and p=="E"):
	print("sim")
	pp -= 18
	print (pp)
elif (pp<18 and p=="E"):
	pp -= 18
	pp *= -1
	print ("nao")
	print (pp)
else:
	print("invalido")

	
	