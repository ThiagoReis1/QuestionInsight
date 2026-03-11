a = float(input("Qual a nota da primeira prova? "))
b = float(input("Qual a nota da segunda prova? "))
c = float(input("Qual a nota da terceira prova? "))
d = float(input("Qual a nota da quarta prova? "))
e = float(input("Qual a nota da quinta prova? "))
m = round((a + b + c + d + e)/ 5,2)
if(m >= 6):
	print(m)	
	print("Aprovado")
else:
	print(m)
	print("Reprovado")
	