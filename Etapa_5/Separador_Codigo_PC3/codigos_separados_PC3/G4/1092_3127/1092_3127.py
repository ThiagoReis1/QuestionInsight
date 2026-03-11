numero=int(input("digite um valor:"))
n1=int(input("primeiro digito:"))
n2=int(input("segundo digito:"))
n3=int(input("terceiro digito:"))
el1=(n1**3)
el2=(n2**3)
el3=(n3**3)
soma=(el1+el2+el3)
if(soma==numero):
	print(numero)
	print("atende")
else:
	print(numero)
	print("nao atende")