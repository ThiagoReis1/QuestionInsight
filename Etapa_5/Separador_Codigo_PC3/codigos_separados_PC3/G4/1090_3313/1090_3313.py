lim = float(input("limite do cartao: "))
a = float(input("compra a: "))
b = float(input("compra b: "))
c = float(input("compra c: "))
d = float(input("compra d: "))
total = a + b + c + d
print(round(total,2))
if(total<=lim):
	print("Dentro do limite")
else:
	print("Estourou o limite")