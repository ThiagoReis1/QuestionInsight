r=input("resultados possiveis:").upper()
p1=3
p2=1
p3=0
jogo=1
resultado=0

while(r!="X"):
		r=input("res:").upper()
		if(r=="V"):
			p1=3
			soma=resultado+p1
			jogo=jogo+1
		elif(r=="E"):
			p2=1
			soma=soma+p2
			jogo=jogo+1
		elif(r=="D"):
			p3=0
			soma=soma+p3
			jogo=jogo+1
total=p1+p2+p3
		
