x = float(input())

if x <= 200:
	total = (5000) + (100*x)
	print(round(total,2))
else:
	total = 8000+ 100*(200)+ 90*(x-200) 
	print(round(total,2))