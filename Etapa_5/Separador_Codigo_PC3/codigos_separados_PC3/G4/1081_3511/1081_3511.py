p1 = float(input("prova1"))
p2 = float(input("prova2"))
p3 = float(input("prova3"))
p4 = float(input("prova4"))
media = ((p1+p2+p3+p4) / 4)
if(media>=5):
	m="Aprovacao"
else:
	m="Reprovacao"

print(round(media,2))
print(m)
