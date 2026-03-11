ca = int(input("consumo de agua: "))

if (ca < 10):
	y = 20 + (2.0 * ca)
if (ca >= 10) and (ca < 20):
	y = 20 + (2.5 * ca)
if (ca >= 20) and (ca < 40):
	y  = 20 + (2.75 * ca)
else:
	y = 20 + (3.0 * ca)
print(round(y, 2))