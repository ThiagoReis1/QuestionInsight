v = float(input())
a = input().upper()
if a == "C":
	h = int(input())
	if h ==1:
		u = 0
	elif h ==2:
		u = v*6/100
	k = v+u
	print(round(k,2))
elif a=="D":
	t = v*11/100
	y = v - t
	print(round(y,2))
elif a=="P":
	t = v*11/100
	l = v-t
	print(round(l,2))
	