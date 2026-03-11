valor=int(input())
an=valor//100000
ran=valor%100000
bn=ran//1000
rbn=ram%1000
cm=rbm//100
rcm=rbm%100
dm=rcm//10
rdm=rcm%10

c= (an*10)**3 + (bn*10)**3 + (dm*10)**3
if (c==valor):
	mensagem="atende"
else:
	mensagem="nao atende"
print(mensagem)
print(valor)
	
	


