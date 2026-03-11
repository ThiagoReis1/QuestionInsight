a=float(input("primeiro valor:"))
b=float(input("segundo valor:"))
c=float(input("terceiro valor:"))

valor= (a+b+c//3)

media= (6)
if(valor > media):
	msg="Aprovacao"

if(valor < media):
	msg="Reprovação"

print(round(valor%media))