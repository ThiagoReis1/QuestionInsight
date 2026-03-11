#cinco provas 
#LEIA: as cinco notas obtidas
#saida: 1 - media aritmetica 2 casas
#aprovacao media>=7,0
#reprovacao por nota media<7
a = float(input("Digite a nota: ")) 
b = float(input("Digite a nota: "))
c = float(input("Digite a nota: "))
d = float(input("Digite a nota: "))
e = float(input("Digite a nota: "))

ma = (a+b+c+d+e)/5
if(ma >= 7.0):

	m = "Aprovacao"
else:
	m = "Reprovacao por nota"
	
print(round(ma,2))
print(m)
