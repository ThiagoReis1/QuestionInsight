#caso seja  x <= 10000 o custo é de 5 reais por hectare
#caso seja x > 10000 o custo é de 5 reais por hectare + 4 reais por excedente

x = float(input("Insira a quantidade da area a ser fertilizada: "))

res = x % 10000
y = x - res
if(x <= 10000):
	c = x * 5
else:
	c = (y * 5) + (res * 4)

z = (res * 4)
print(round(c, 2))