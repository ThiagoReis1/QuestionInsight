c = float(input("Quantidade de combustivel comum: "))

if (c > 0) and (c < 17.5):
	t = 10.5
	
elif (c > 17.5) and (c < 35.0):
	t = 14.0
	
elif (c > 35.0) and (c < 50.0):
	t = 18.6
	
else:
	t = 24.5
	
s = t + c
print(round(s, 1))