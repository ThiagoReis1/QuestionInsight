ano = 2023
nasc = int(input("Digite o ano de seu nascimento: "))
pais = input("Digite (j) para Japao ou (b) para Brasil: ")
pais = pais.upper()
idade = 2023 - nasc
japao = idade - 16
brasil = idade - 18
japao2 = 16 - idade
brasil2 = 18 - idade
if idade >= 16 and pais == "J":
 print("sim")
 print(japao)
elif idade < 16 and pais == "J":
 print("nao")
 print(japao2)
elif idade >= 18 and pais == "B":
 print("sim")
 print(brasil)
elif idade < 18 and pais == "B":
 print("nao")
 print(brasil2)
elif pais != "J" or pais != "B":
 print("invalido")
	
	

 