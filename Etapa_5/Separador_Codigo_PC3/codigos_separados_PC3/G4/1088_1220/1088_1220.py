nA= float(input("Digite a primeira nota: "))
nB= float(input("Digite a segunda nota: "))
nC= float(input("Digite a terceira nota: "))
nD= float(input("Digite a quarta nota: "))
nE= float(input("Digite a quinta nota: "))
media=(nA+nB+nC+nD+nE)/5
print (round(media, 2))
if(media >=7):
	print("Aprovacao")
else:
	print("Reprovacao")