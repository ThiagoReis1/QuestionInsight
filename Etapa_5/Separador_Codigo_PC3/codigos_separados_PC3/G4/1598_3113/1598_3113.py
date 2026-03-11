from numpy import*

a = array(eval(input("custo dos itens:")))

i=0
p = 80.00
desconto = 5
descontofinal = 0


while(i < size(a)):
	if(a[i] > p):
		descontofinal = descontofinal + desconto
	i = i + 1
na = sum(a)
s = na - descontofinal

print(round(s,2))

# os itens q voce compra acima de 80, ganham desconto de 5 na compra total


