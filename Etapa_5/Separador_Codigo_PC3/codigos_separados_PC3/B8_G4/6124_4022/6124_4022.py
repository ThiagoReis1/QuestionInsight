p = float(input())

#if (p < 3000) or (p> 4500):
#	print("nao e bb")

if (p >= 3000) and (p < 3400):
	gas = 0.8 * p
	print(round(gas, 1))

elif (p >= 3400) and (p < 3900):
	gas = 1.3 * p
	print(round(gas, 1))
	
elif (p >= 3900) and (p < 4100):
	gas = 2.1 * p
	print(round(gas, 1))

elif (p >= 4100) and (p<= 4500):
	gas = 3 * p
	print(round(gas, 1))