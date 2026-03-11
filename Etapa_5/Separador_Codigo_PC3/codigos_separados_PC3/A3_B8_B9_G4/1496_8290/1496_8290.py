tv = int(input('tempo de voo: '))
vt = 0

if (tv <= 100):
	vt = tv * 80 + 3000
	
elif (tv > 100 and tv <= 200):
	vt = tv * 90 + 4000
	
elif (tv > 200 and tv <= 300):
	vt = tv * 100 + 5000
	
elif (tv > 300):
	vt = tv * 110 + 6000
	
print(round(vt, 2))
