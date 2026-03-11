#entrada
prova1 = float(input("digite nota 1:"))
prova2 = float(input("digite nota 2:"))
prova3 = float(input("digite nota 3:"))
prova4 = float(input("digite nota 4:"))
prova5 = float(input("digite nota 5:"))
#formula
nota_total = (prova1 + prova2 + prova3 + prova4 + prova5) / 5

if(nota_total >= 6):
	situacao = "Aprovado"
else:
	situacao = "Reprovado"
print (round(nota_total , 2))
print (situacao)