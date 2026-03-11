d = float(input())
f = input().upper()

if f== "D" or f == 'P':
	tt = d* 0.82
	print(round(tt,2))
elif f == "C":
	c= int(input())
	if c == 1:
		tt = d
	elif c == 2:
		tt = d + (d*0.07)
	print(round(tt,2))