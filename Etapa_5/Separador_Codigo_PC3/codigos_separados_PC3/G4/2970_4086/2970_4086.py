qi= float(15)
qf=float(104200)
t=int(input("meses: "))
i=((qf/qi)**(1/t)) - 1

if (i <= 0.01):
	mensagem= "real"
	
else:
	mensagem="irreal"
print(round(i ))
print(mensagem)