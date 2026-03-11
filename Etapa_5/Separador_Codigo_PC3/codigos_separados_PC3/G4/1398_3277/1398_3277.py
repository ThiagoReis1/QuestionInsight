a=float(input("Tempo de voo: "))
c=(100*a) + 5000
c1=(100*200)+(90*(a-200)) + 8000
if (a<=200):
	print(round(c,2))
else:
	print(round(c1,2))
	