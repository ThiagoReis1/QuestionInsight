a= int(input("numero "))

if(0 < a < 17.5):
	t= a+0.8
	print(t)
elif(17.5 <= a <= 35.0):
	t= a+1.3
	print(t)
elif(35.0 <= a <= 50.0):
	t= a+2.1
	print(t)
else:
	t=a+3.0
	print(t)