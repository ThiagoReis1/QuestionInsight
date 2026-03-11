H = int(input("Quantos habitantes:"))
V = int(input("Quantos vampiros :"))
X = int(input("Transformados:"))
Y = int(input("Vampiros mortos:"))

i = 0
acumulador = V 
while(acumulador <= H ):
		acumulador = (acumulador + (acumulador * X ) - Y)
		i = i + 1
print(i)
