p1 = float(input("prova um: "))
p2 = float(input("prova dois: "))
p3 = float(input("prova tres: "))
p4 = float(input("prova quatro: "))

soma=p1+p2+p3+p4
media=soma/4
if (media>=5):
	print(round(media,2),"Aprovacao")
else:
	print(round(media,2),"Reprovacao")
