d = float(input())
t = float(input())

p = ((d*1000) / 10) * 30

if(t >= p):
	print(round(p,2))
	print("vai conseguir")
else:
	print(round(p,2))
	print("nao vai consegui")