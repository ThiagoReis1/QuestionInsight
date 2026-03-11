comum = float(input("Qual a quantidade de combustivel comum?: "))

if (comum < 17.5):
	total = comum + 0.8
	
elif (comum >= 17.5 and comum < 35.0):
	total = comum + 1.3
	
elif (comum >= 35 and comum < 50.0):
	total = comum + 2.1
	
elif (comum >= 50):
	total = comum + 3.0
	
print(round(total, 1))