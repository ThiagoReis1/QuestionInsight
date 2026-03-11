tv= int(input("tempo de voo: "))
ct1= float(round((5000 + 100 * tv),2))
ct2= float(round((8000 + 100 * 200 + 90 * (tv - 200)),2))

if(tv <= 200):
	print(ct1)
else:
	print(ct2)
	