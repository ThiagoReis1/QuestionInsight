#Johnathan Dias			#Matricula:21651445
#Avaliacao					#Data:27/07/2016
N=int(input("digitar um numero inteiro:"))
cont=1
div=3
sinal=-1
S=0
while(cont<= N):
	S = S - sinal * (cont**3)/(2+div)
	sinal = -sinal
	cont = cont+1
	div = div+2
print(round(S,8))