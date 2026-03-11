amin = input()

if(amin.lower() == "leucina"):
	peso = 6*12.011 + 13*1.0079 + 14.00674 + 2*15.9994
	print(round(peso,2))
else:
	peso = 6*12.011 + 15*1.0079 + 2*14.00674 + 2*15.9994
	print(round(peso,2))
