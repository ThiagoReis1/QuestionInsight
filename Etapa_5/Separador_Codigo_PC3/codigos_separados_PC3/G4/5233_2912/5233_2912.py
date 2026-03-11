num = int(input())
if(num%3==0 and num%5!=0):
	print("Auau")
elif(num%5==0 and num%3!=0):
	print("Miau")
elif(num%5==0 and num%3==0):
	print("AuauMiau")
else:
	print(num)