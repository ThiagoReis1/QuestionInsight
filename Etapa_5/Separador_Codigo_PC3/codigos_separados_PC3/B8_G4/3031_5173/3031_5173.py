num = float(input("entre com o valor de x: "))

if(num <= 1):
	f = 1
elif(1 < num and num <=2):
	f = 2
elif(2 < num and num <=3):
	f = num**2
elif(num > 3):
	f = num**3
print(round(f, 2))