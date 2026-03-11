#Igor Rodrigues Chicolet da SIlva
#Universidade Federal do Amazonas - UFAM
#Num de matricula: 21204615 - 13/07/2016

ida = int(input("Qual e a idade da pessoa? ")) #idade
ps = float(input("Qual e o peso da pessoa? ")) #peso


if((ida > 0) and (ida <= 20) and (ps > 0) and (ps <= 60)):
	gr = 9
elif((ida > 0) and (ida <= 20) and (ps > 60) and (ps <= 90)):
	gr = 8
elif((ida > 0) and (ida <= 20) and (ps > 90) and (ps < 550)):
	gr = 7
elif((ida > 20) and (ida <= 50) and (ps > 0) and (ps <= 60)):
	gr = 6
elif((ida > 20) and (ida <= 50) and (ps > 60) and (ps <= 90)):
	gr = 5 
elif((ida > 20) and (ida <= 50) and (ps > 90) and (ps < 550)):
	gr = 4
elif((ida > 50) and (ida < 130) and (ps > 0) and (ps <= 60)):
	gr = 3
elif((ida > 50) and (ida < 130) and (ps > 60) and (ps <= 90)):
	gr = 2
elif((ida > 50) and (ida < 130) and (ps > 90) and (ps < 550)):
	gr = 1
else:
	gr = -1

print("Entradas:", ida, "anos e", ps, "kg")
if(gr == -1):
	print("Dados invalidos")
else:
	print("Grupo de risco:", gr)