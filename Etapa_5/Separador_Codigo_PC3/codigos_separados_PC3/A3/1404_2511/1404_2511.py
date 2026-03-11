#Demogorgon

nome_da_cabeca = input("Aameul/Hethradiah? ")
dado_a = int(input("Digite a face de 0 a 10?: "))
dado_b = int(input("Digite a face de 0 a 10?: "))
dado_c = int(input("Digite a face de 0 a 10?: "))
Aameul_dano_fixo = 8
soma_das_faces = dado_a + dado_b + dado_c
Aemul_dano_aleatorio = soma_das_faces
raio_Aameul = Aameul_dano_fixo + Aemul_dano_aleatorio
Olhar_Hethrediah = 2 * soma_das_faces
pontos_de_Demogorgon_perdidos = raio_Aameul + Olhar_Hethrediah
pontos_de_Demogorgon_perdidos = raio_Aameul + Olhar_Hethrediah
if(nome_da_cabeca=="Aameul"):
	raio_Aameul = Aameul_dano_fixo + Aemul_dano_aleatorio
	print(raio_Aameul)
else:
	Olhar_Hethrediah = 2 * soma_das_faces
	print(Olhar_Hethrediah)
