A= input("T se for torta ou P se for pastel: ").upper()
Q= int(input("quantidade de fatias de tortas ou pastel: "))
C= int(input("quantidade de cappuccinos: "))

if A=="T":
	total=(Q*6) + (C*4.50)
	print(total)
else:
	total=(Q*5)+ (C*4.50)
	print(total)
	
	