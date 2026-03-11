c= float(input("consumo de energia:"))

if (c<=150):
	v= 0.60*c + 5.00
else:
	v= 0.75*c + 16.00
print(round(v,2))