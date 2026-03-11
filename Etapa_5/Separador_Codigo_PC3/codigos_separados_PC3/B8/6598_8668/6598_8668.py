# faça seu código aqui!
N = int(input("integrantes: "))
cont = 0
votos_tais = 0
votos_edgar = 0
votos_ana = 0

while (cont < N):
	professor = input("nome do professor: ").lower()
	if (professor == "tais"):
		votos_tais += 1
	elif (professor == "edgar"):
		votos_edgar += 1
	elif (professor == "ana"):
		votos_ana += 1
	cont += 1	
print("tais=", votos_tais)
print("edgar=", votos_edgar)
print("ana=", votos_ana)