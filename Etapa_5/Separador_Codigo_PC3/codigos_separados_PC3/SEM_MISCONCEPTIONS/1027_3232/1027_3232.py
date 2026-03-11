consumo = float(input())
a = 10 + (0.43*consumo)
icms = a*0.25

total = a + icms
print(float(round(total, 2)))