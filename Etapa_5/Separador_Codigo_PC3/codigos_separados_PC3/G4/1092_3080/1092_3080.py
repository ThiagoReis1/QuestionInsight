n=int(input()) #numero informado
n1= n // 100 #numero 1
n1r= n % 100 #resto do numero 1
n2= (n%100) // 10 #numero 2
n3= n1r % 10 #numero 3
#calculo dos numeros ao cubo
calculo= (n1 ** 3) + (n2 ** 3) + (n3 ** 3)
if(calculo == n):
	mensagem= "atende"
else:
	mensagem="nao atende"
print(n)
print(mensagem)




