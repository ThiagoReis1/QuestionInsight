# andrea cristina de lima lopes
#matricula 21552445
# avaliacao 02

X=int(input())
Xp1= X // 1000
Xparte2= X % 1000
viX=(Xp1-Xp2)**2
if(viX == X):
	mensagem =" X atende a propriedade"
else:
	mensagem = viX
print(mensagem)
	