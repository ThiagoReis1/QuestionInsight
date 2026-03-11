x = float(input("valor de x: "))
k = int(input("valor de K: "))
res = 0 
i = 1
while(k != 0):
	res = res + (x/ (i * 2)) 
	i = i + 1
	k = k - 1
print(round(res,8))