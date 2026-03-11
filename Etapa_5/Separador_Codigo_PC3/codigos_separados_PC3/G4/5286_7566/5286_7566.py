x = int(input("insira um numero: "))
e = 0 
k = 0
while(x != 0):
	if(x%2 == 0):
		k = k + 1
	e = e + 1
	x = int(input("insira um numero: "))
y = (k/e)*100
print(e)
print(round(y, 2))
	