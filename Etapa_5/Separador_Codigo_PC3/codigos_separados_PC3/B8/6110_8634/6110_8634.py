rfuel = float(input("Quantidade de combustivel comum: "))

if rfuel < 17.5:
	total= rfuel + 10.5
elif 17.5 <= rfuel < 35.0:
	total= rfuel + 14.0
elif 35.0 <= rfuel < 50.0:
	total = rfuel + 18.6
elif rfuel >= 50.0:
	total = rfuel + 24.5
	
print(round(total, 1))