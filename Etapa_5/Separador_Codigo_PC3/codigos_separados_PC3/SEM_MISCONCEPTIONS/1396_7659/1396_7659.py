consumo = float(input("digite o valor:"))

a = (consumo*10)/100
b = (consumo*6)/100

total1 = a + consumo
total2 = b + consumo

if(consumo>300):
	msg = total2
else:
	msg = total1

print(round(msg, 2))