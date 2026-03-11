nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

t1 = (nota1+nota2+nota3)/3

if(t1 >= 7):
   media = "Aprovado"
else:
	media = "Reprovado"
print(round(t1,1),media)
	

