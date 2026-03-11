area = float(input())
if area >= 0:
	if (area>=0) and (area<100):
		v = (area*2)+100
	elif (area>=100) and (area<2500):
		v = (area*1.80)+150
	elif (area>=2500) and (area<10000):
		v = area*1.50+200
	elif (area>10000):
		v = (area*1.20)+250
		
print(round(v,2))