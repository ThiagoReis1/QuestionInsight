L = 5.0
S = 3.5
R = 4.0

a = input("Digite L para lanche ou S para salgado: ")
b = int(input("quantidade de comida: "))
c = int(input("Quantidade refri: "))
 
if a == "L":
	total = b * L
elif a == "S":
	total = b * S
total1 = total + c * R

print(total1)
