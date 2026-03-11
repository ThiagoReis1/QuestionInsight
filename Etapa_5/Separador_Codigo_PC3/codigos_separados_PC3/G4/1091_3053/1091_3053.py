num = int(input("Digite o numero: "))
a = num//100
r1 = num%100
b = r1
x = (a+b)**2
if (num==x):
	m = "atende"
else:
	m = "nao atende"
print(num)
print(m)
	