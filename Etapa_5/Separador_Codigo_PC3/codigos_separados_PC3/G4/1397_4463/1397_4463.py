area = int(input("Digite um numero: "))

adc = area - 10000

if (area <= 10000):
	msg = 5 * area
else: 
	msg = 5 * 10000 + 4 * adc

print(round(msg, 2))
