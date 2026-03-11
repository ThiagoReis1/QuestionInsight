pc=int(input("informe a posicao: "))
soma=0
while(pc!=0):
	if(pc==1):
		pnt=20
		soma=soma+pnt
	else:
		if(pc==2):
			pnt=15
			soma=soma+pnt
		else:
			if(pc==3):
				pnt=10
				soma=soma+pnt
			else:
				if(4<=pc<=10):
					pnt=(11-pc)
					soma=soma+pnt
				else:
					pnt=0
					soma=soma+pnt
	pc=int(input("informe a posicao: "))
print("total=",soma,"pontos")
	