# faça seu código aqui!
p = int(input("Horario do pedido: "))
q = int(input("quantidade: "))

s = q *28.5

if (p >= 18):
	t = s - (s * (20/100))
else: 
	t = s
print(round(t, 2))