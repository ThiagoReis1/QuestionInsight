nome = input("arginina ou tirosina: ")
O = 15.9994
C = 12.011
N = 14.00674
H = 1.00794
arginina = (O*2)+(C*6)+(N*4)+(H*15)
tirosina = (O*3)+(C*9)+(N)+(H*11)

if(nome.upper() == "ARGININA"):
	mensagem = (O*2)+(C*6)+(N*4)+(H*15)

else:
	mensagem = (O*3)+(N)+(H*11)+(C*9)

print(round(mensagem,2))