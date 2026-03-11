nhb = int(input("informe o numero de habitantes: "))
nhp = int(input("informe o numero de habitantes: "))
nhpr = int(input("informe o numero de habitantes: "))
tx_nhb = float(input("informe a taxa anual de crescimento: "))
tx_nhp = float(input("informe a taxa anual de crescimento: "))
tx_nhpr = float(input("informe a taxa anual de crescimento: "))

a = nhb
b = nhp
c = nhpr
i = 0
d = 0
while (c > d ):
	a = a + (a* tx_nhb/100)
	b = b + (b* tx_nhp/100)
	d = a + b
	c = c + (c* tx_nhpr/100)
	i = i + 1
print(i)