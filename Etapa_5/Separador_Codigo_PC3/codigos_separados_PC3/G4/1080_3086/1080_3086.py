x = float(input("digite a nota aqui: "))
y = float(input("digite a nota aqui: "))
z = float(input("digite a nota aqui: "))
ma = (x + y + z)/3
if(ma >= 5):
	msg = "Aprovado"
else:
	msg = "Reprovado"
print(round(ma, 1))
print(msg)