tem= float(input("tempo de voo em minutos: "))

if tem <= 200:
	
	vt=5000+100*tem
	print(round(vt,2))
	
else:
	
	vt=8000+ 100*200 + 90*(tem-200)
	print(round(vt,2))