nf = int(input("numero de 4 digitos fornecido: "))

num1 = nf // 100
num2 = nf % 100


calc = (num1)**2 + (num2)**2

if(nf == calc ):
	msg = "atende"
else:
	msg = "nao atende"
print(msg)
print(nf)