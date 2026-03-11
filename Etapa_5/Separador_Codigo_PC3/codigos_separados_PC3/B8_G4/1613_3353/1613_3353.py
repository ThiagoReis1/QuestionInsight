from numpy import*

atv=array(eval((input("digite os Atividades: "))))
d=array(eval(input("digite as duracoes: ")))
i=0
soma=0

tma=size(atv)
while(i<tma):
	if(atv[i]=="ALONGAMENTO"):
		soma=soma+(d[i]*3)
	elif(atv[i]=="CORRIDA"):
		soma=soma+(d[i]*10.3)
	elif(atv[i]=="DANCA"):
		soma=soma+(d[i]*6.7)
	elif(atv[i]=="ESCALADA"):
		soma=soma+(d[i]*9.7)
	elif(atv[i]=="HIDROGINASTICA"):
		soma=soma+(d[i]*5)
	i=i+1

print(round(soma,2))