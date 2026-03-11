vl=int(input())
a= vl//1000
ra=vl%1000
c=(a-ra)**2
if (vl==c):
	mensagem="atende"
else:
	mensagem="nao atende"
print(mensagem)
print(vl)