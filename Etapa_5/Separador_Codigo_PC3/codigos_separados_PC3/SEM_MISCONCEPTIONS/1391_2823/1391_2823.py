x= float(input("consumo:"))

if (x <= 150):
	valor= x*0.60 + 5
else:
	valor= x*0.75 + 16 
	
print(round(valor,2))