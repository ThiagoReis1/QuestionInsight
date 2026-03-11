limite= float(input())
valor_a=float(input())
valor_b=float(input())
valor_c=float(input())
valor_d=float(input())
valor_total=valor_a+valor_b+valor_c+valor_d

if (valor_total<=limite):
   mensagem="Dentro do limite"
else:
	mensagem="Estourou o limite"
print(round(valor_total,2))
print(mensagem)