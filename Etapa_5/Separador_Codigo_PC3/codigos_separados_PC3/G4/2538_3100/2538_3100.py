s = float(input())
d = float(input())
m = float(input())
j = float(input())
t = 0
if (s>0 and d>0 and m>0 and j>0):
	while(d <= s):
		d = round(d + m + (d * j/100), 2)
		t = t + 1
	print(t)
else:
	print("Dados incorretos")
		
	