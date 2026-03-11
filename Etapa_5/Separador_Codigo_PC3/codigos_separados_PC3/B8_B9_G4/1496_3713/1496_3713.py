m = float(input())

if(m < 100):
	c = m * 80 + 3000
	print(round(c, 2))
elif((m >= 100) and (m < 200)):
	c = m * 90 + 4000
	print(round(c, 2))
elif((m >= 200) and (m < 300)):
	c = m * 100 + 5000
	print(round(c, 2))
elif(m >= 300):
	c = m * 110 + 6000
	print(round(c, 2))

	
