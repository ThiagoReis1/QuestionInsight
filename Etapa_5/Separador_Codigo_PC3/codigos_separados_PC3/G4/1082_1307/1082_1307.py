p1 = float(input("Digite a nota da primeira prova: "))
p2 = float(input("Digite a nota da segunda prova: "))
p3 = float(input("Digite a nota da terceira prova: "))
p4 = float(input("Digite a nota da quarta prova: "))
p5 = float(input("Digite a nota da quinta prova: "))

nf = (p1 + p2 + p3 + p4 + p5) / 5

print(round(nf,1))

if (nf < 5):
	  print("Reprovado")
else:
	  print("Aprovado")