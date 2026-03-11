#provas
p1 = float(input("entre com a nota da prova: "))
p2 = float(input("entre com a nota da prova: "))
p3 = float(input("entre com a nota da prova: "))
p4 = float(input("entre com a nota da prova: "))
p5 = float(input("entre com a nota da prova: "))
med = (p1 + p2 + p3 +p4 + p5)/5
if(med>=7.0):
	mensagem = "Aprovacao"
else:
	mensagem = "Reprovacao por nota"
print(round(med,2))
print(mensagem)
