L = 6
P = 13.5
R = 3

TipoPrato = input("Qual tipo de prato: ")
QComida = int(input("Quantos pratos: "))
QRefri = int(input("Quantos Refris: "))

if TipoPrato == "P":
	print(round(((P*QComida)+(R*QRefri)),2))
if TipoPrato == "L":
	print(round(((L*QComida+R*QRefri)),2))