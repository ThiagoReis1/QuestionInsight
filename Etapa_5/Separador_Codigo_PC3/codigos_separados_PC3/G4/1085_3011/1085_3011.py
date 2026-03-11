a=float(input("Nota 1:"))
b=float(input("Nota 2:"))
c=float(input("Nota 3:"))
d=float(input("Nota 4:"))
e=float(input("Nota 5:"))
m=(a+b+c+d+e)/5
if (m >= 6.0):
	mensagem="Aprovacao"
else:
	mensagem="Reprovacao"
print(round(m,2))	
print(mensagem)