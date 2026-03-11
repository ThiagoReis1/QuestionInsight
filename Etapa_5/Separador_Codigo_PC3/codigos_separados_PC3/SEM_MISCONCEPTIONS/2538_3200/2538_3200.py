valorsitio= float(input())
valorinicial= float(input())
depositomen= float(input())
juros= float(input())

cont=0
soma=0
juros= juros/100
if(valorsitio>0 and depositomen>0 and valorinicial>0 and juros>0):
	while(valorsitio>soma):
		atual= valorinicial + depositomen
		calcj= (atual*juros)/100
		calc= atual - calcj
		soma= calc + soma
		cont= cont+1
	print(atual)
else:
	print("Dados incorretos")