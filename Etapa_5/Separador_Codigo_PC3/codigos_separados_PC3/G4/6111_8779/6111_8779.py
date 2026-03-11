x= float(input())
if x<17.5:
	t= x+10.5
	print(round(t, 1))
elif 17.5<=x<=35.:
	t= x+14.
	print(round(t, 1))
elif 35.<=x<=50.:
	t= x+18.6
	print(round(t, 1))
else:
	t= x+24.5
	print(round(t, 2))