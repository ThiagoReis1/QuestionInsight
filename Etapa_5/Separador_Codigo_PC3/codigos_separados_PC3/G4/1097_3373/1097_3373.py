valor=int(input())
am=valor//100000
ram=valor%100000
bm=ram//10000
rbm=ram%10000
cm=rbm//1000
rcm=rbm%1000
dm=rcm//100
rdm=rcm%100
em=rdm//10
rem=rdm%10
fm=rem//1
c=((am*100+bm*10+cm)-(dm*100+em*10+fm))**2
if (c==valor):
	mensagem="atende"
else:
	 mensagem="nao atende"
print(mensagem)
print(valor)