num = int(input())
horas = int(input())

cont = 0

while cont < horas:
	num = num + int((num * 0.02))
	cont = cont + 1
print(num)

