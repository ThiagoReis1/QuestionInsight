nascimento = int(input("Digite o ano de nascimento: "))
pais = input("Qual o pais que deseja verificar(B/R): ")
ano = 2023
if pais == "B" and nascimento <= 2002:
	apto = "sim"
	print(apto)
	passou = (ano - nascimento) - 21
	print(passou)

elif pais == "B" and nascimento > 2002:
	apto = "nao"
	print(apto)
	falta = 21 - (ano - nascimento)
	print(falta)
	
if pais == "R" and nascimento <= 2005:
	apto = "sim" 
	print(apto)
	passou = (ano - nascimento) - 18
	print(passou)

elif pais == "R" and nascimento > 2005:
	apto = "nao"
	print(apto)
	falta = 18 - (ano - nascimento)
	print(falta)
	
if pais != "B" and pais != "R":
	a = "invalido"
	print(a)