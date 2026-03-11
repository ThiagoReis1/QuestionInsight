a=int(input("qual a area a ser fertilizada?"))
b= a<=10
c= a>=10
if(b):
	mensagem = 5.00*a
else:
	mensagem = (5.00*b)+(4.00*c)
print(round(mensagem,2))