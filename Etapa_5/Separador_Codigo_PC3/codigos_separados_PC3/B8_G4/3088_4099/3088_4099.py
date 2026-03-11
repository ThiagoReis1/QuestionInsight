x = int(input("numero: "))

P = 0
I = 0
while(x != 0):
	if(x%2 == 0):
		P = P + 1
		
	else:
		if(x%2 != 0):
			I = I + 1

todo = (P + I)/100
par = (P / todo) - 100
impar = (I * todo) - 100

print(round(par, 2))
print(round(impar, 2))
	
	