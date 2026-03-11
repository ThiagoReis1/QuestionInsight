a= int(input())
p= input().upper()
i= 2023-a
if (p=="B"):
	if (i>=21):
		apt= i-21
		print ("sim")
		print (apt)
	elif (i<21):
		napt= 21-i
		print ("nao")
		print (napt)
elif(p=="R"):
	if (i>=18):
		apt= i-18
		print("sim")
		print(apt)
	elif (i<18):
		napt= 18-i
		print ("nao")
		print (napt)
else:
	print("invalido")
		