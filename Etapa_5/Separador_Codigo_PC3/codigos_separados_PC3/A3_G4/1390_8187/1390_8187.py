con= float(input("min: "))
lim= 100
if(con <= 100):
	cal= con*1.20
else:
	cal= con*1.40+25.00
print(round(cal,2))