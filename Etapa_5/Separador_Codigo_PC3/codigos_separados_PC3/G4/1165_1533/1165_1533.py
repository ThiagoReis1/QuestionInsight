n = int(input("n: "))
num = 1
den = 1
i = 1
var = 0
while(i<=n):
	if(i%2==0):
		var = var -((num**3)/(5+den))
	else:
		var = var+ ((num**3)/(5+den))
	i = i+1
	num = num +1
	den = den +2
print(round(var, 9))