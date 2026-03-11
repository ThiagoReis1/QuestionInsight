nome=input("Digite o nome do aminoacido: ")
O=15.9994
C=12.011
N=14.0067
H=1.00794
if(nome.upper()=="GLUTAMINA"):
	soma=((C*5)+(H*8)+(N*1)+(O*4))
	print(round(soma,2))
elif(nome.upper()=="SERINA"):
	soma=((C*3)+(H*7)+(N*1)+(O*3))
	print(round(soma,2))
elif(nome.upper()=="TREONINA"):
	soma=((C*4)(H*9)+(N*1)+(O*3))
	print(round(soma,2))
else:
	print("Entrada:", nome)
	print("Dado Invalido")

