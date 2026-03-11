a = float(input())
b = float(input())
c = float(input())
d = float(input())

k = a*7
l = b*6
m = c*3
n = d*5

val = k+l+m+n

if(val<=42.0):
	x = round(val-3.0, 2)
	print(x,"ryous")
else:
	x = (10/100)*val
	y = val-x
	print(y,"ryous")