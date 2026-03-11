pv=int(input("quantidade inicial de pontos de vida:"))
a=int(input("primeiro valor:"))
b=int(input("segundo valor:"))
c=int(input("terceiro valor:"))
x=10*(a+b+c) -pv
y=pv-10*(a+b+c)
if (y>0):
	print(y)
	print("VIVO")
else:
	print("0")
	print("MORTO")