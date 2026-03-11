# faça seu código aqui!
dia = input()
pratos = int(input())
total = pratos * 22.00
if(dia == "qua"):
	total = total * 0.85
print(round(total, 2))