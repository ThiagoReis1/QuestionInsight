from numpy import*
r = array(eval(input("digite o nmr de vetores:")))
i = 0
pr = 200
while i < size(r):
	if	r[i] == 1:
	  	pr = pr / 2
	elif r[i] == 2:
		 pr = pr * 3
	elif r[i] == 3:
		pr = pr / 2
	elif r[i] == 4:
		pr = pr * 3
	elif r[i] == 5:
		pr = pr / 2
	elif r[i] == 6:
		pr = pr * 3
	i = i + 1
print(round(pr,2))			
