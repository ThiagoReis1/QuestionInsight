x = float(input("Digite x: "))
k = int(input("Digite o termo k: "))
s = 0
i = 0
k=k-1
if(x > -1 and x < 1):
	while(i <= k):
		s = s + (((-1)**i) * (x**i))
		i = i + 1
	print(round(s,7))