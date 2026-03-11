comum = float(input("digite qt da comum: "))
if comum < 17.5: 
	total = comum + 1.5
elif 17.5 <= comum < 35.0: 
	total = comum + 2.3
elif 35.0 <= comum < 50.0: 
	total = comum + 3.3
elif comum >= 50.0: 
	total = comum + 4.7
print(round(total, 1))