#Luiz Inácio
#Av 02 Ex.01


a=float(input("Insira a nota N01:"))
b=float(input("Insira a nota N02:"))
c=float(input("Insira a nota N03:"))
d=float(input("Insira a nota N04:"))

e=float((a+b+c+d)/4)
print (round(e,2))
if e>=7:
	print ("Aprovado")
else:
	print ("Reprovado")