# faça seu código aqui!
diarias = 175

dias = int(input("Informe a quantidade de dias que deseja se hospedar: "))
if dias < 15:
	hospedagem = diarias*dias+20
elif dias == 15:
	hospedagem = diarias*dias+16
elif dias > 15:
	hospedagem = diarias*dias+10
	
print (round(hospedagem,2))