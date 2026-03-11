esc = (input(""))
vltemp= float(input(""))

if(vltemp >= 0):
	k = c + 237.15
	vltemp = k
if(vltemp <= 0):
		c = k - 237.15
		vltemp = c
print(round(vltemp , 2))