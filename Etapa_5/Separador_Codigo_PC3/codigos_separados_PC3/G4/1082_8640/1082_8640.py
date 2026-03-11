p1= float(input("nota1"))
p2= float(input("nota2"))
p3= float(input("nota3"))
p4= float(input("nota4"))
p5=float(input("nota5"))

pq = ((p1 + p2 + p3 + p4 +p5) / 5)
		  
if pq >= 5.0:
	print(round(pq,1))
	print("Aprovado")
else:
	print(round(pq,1))
	print("Reprovado")

				
		