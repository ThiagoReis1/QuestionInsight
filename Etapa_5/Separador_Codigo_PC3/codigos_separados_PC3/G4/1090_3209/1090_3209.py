lim = float(input("insira um valor: "))
a = float(input("insira um valor: "))
b = float(input("insira um valor: "))
c = float(input("insira um valor: "))
d = float(input("insira um valor: "))

total = a+b+c+d
print(round(total,2))
if (total<=lim):
	print("Dentro do limite")
else: 
	print("Estourou o limite")