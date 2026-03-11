from numpy import *
tipo = array(eval(input("Insira um vetor de strings do tipo de magia: ")))
nivel = array(eval(input("Insira um vetor de numeros do nivel do mago:")))
dano = 0
dano_total = 0
i=0
while:
	if (tipo[i] == "GELO"):
		dano_total = dano + 2 * nivel
		dano = dano_total
	if (tipo[i] == "FOGO"):
		dano_total = dano + 3 * nivel
		dano = dano_total
	if (tipo[i] == "CHOQUE"):
		dano_total = dano + 4 * nivel
		dano = dano_total
	if(tipo[i] == "CONJURACAO"):
		dano_total = dano + 8 * nivel
		dano = dano_total
	if(tipo[i] == "ILUSAO"):
		dano_total = dano + 10 * nivel
		dano = dano_total
print(dano_total)