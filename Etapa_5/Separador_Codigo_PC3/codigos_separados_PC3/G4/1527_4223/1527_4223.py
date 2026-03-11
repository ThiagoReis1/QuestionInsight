f=int(input("Digite a quantidade inicial de seguidores do deus f: "))
l=int(input("Digite a quantidade inicial de seguidores do deus l: "))
pf=float(input("Digite o percentual anual: "))
pl=float(input("Digite o percentual anual: "))

ano=0

while(l<f):
	l=l+(pl/100)*l
	f=f+(pf/100)*f
	ano=ano+1
print(ano)
	
