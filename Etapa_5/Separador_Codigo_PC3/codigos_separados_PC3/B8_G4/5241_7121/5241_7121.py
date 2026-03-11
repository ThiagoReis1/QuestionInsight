x = int(input("Consumo de agua: "))

if x < 10 :
	s = 20 + (2*x)
elif 10 <= x < 20: 
	s = 20 + (2.5 * x)
elif 20 <= x < 40:
	s = 20 + (2.75 * x)
elif x >= 40 : 
	s = 20 + (3 * x)

print(round(s, 2))