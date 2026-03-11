n1 = float(input("informe a primeira nota: "))
n2 = float(input("informe a segunda nota: "))
n3 = float(input("informe a terceira nota: "))
n4 = float(input("informe a quarta nota: "))

media = round((n1 + n2 + n3 + n4)/4,2)

if ( media >= 7 ):
	
	print(media)
	print("Aprovado")
	
else:
	
	print(media)
	print("Reprovado")