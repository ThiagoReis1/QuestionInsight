from numpy import*
dano = array(eval(input('vetor de dano: ')))
i = 0 # contador (controla a posiçao do vetor)
p = 1 # o peso por ataque (tem q ser o anterior mais um)
d = 0 # o dano cada golpe somado com o anterior (saida)
while i < size(dano) :
	d = d + dano[i] * p 
	i = i + 1
	p = p + 1
print(int((d)))
	