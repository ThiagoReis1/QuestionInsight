p1=float(input("digite o valor da prova:"))
p2=float(input("digite o valor da prova:"))
p3=float(input("digite o valor da prova:"))
media= ((p1+p2+p3)/3)

print(round(media,1))

if(media>=7):
		print("Aprovado")
else:
		print("Reprovado")