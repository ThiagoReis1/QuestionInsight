a = float(input("area: "))

if 0 <= a <= 10000:
	v = (a*6)+100
elif 10001 <= a <= 20000:
	v = (a*5.5) + 150
elif 200001 <= a <= 30000:
	v = (a*5)+200
elif a < 30000:
	v = (a*4.5)+250
print(round(v,2))