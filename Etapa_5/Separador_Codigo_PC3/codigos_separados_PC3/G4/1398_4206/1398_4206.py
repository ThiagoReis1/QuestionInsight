a = float(input())
b = 5000+(100*a)
c = 8000+(200*100)+((a-200)*90)
if(a<=200):
	print(round(b,2))
else:
	print(round(c,2))