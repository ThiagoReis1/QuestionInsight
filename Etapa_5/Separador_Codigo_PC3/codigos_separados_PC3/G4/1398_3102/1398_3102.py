t = float(input("tempo de voo"))

a1= 5000 + 100*t
a2= 8000 + 100*200 + 90*(t-200)

if(t<=200):
	print(round(a1,2))
else:
	print(round(a2,2))