quantos elementos sao pare, quantos sao impares e quantos tem

from numpy import *
vet = array(eval(input("Informe o vetor:")))
while (size(vet) > 1):
	cpar = 0
	for e in vet:
		if (e % 2 == 0):
			cpar = cpar + 1
	print(cpar)
	print(size(vet) - cpar)
	print(size(vet))
vet = array(eval(input("Informe o vetor:")))


aprovado mas nao pode ser monitor
##########################################################
from numpy import *
vet = array(eval(input("Informe o vetor:")))
while (size(vet) > 1):
	cont = 0
	for e in vet:
		if (5 <= e < 7):
			cont = cont + 1
	print(cont)
	vet = array(eval(input("Informe o vetor:")))
    
    
contar ocorrencias 1 time de futebol
##########################################################

from numpy import *
vet1 = array(eval(input("Informe o vetor de gol feitos:")))
vet2 = array(eval(input("Informe o vetor de gols tomados:")))
vet3 = array([0,0,0])
for ind in range(size(vet1)):
	if (vet1[ind] > vet2[ind]):
		vet3[0] = vet3[0] + 1
	elif (vet1[ind] == vet2[ind]):
		vet3[1] = vet3[1] + 1
	else:
		vet3[2] = vet3[2] + 1
print(vet3)

contar ocorrencia 2 aprovação em discipline
#########################################################

from numpy import *
notas = array(eval(input("Notas:")))
freq = array(eval(input("Frequencias:")))
carga = int(input("Carga horaria:"))
vet = array([0,0,0])
for ind in range(size(notas)):
	if (freq[ind] < carga * 0.75):
		vet[2] = vet[2] + 1
	elif (notas[ind] >= 5.0):
		vet[0] = vet[0] + 1
	else:
		vet[1] = vet[1] + 1
print(vet)

contar ocorrencia 3 faltas ao trabalho
#########################################################

from numpy import *
vet_faltas = array(eval(input("Faltas:")))
vet_semana = array([0,0,0,0,0,0])
vet_percentual = array([0.0,0.0,0.0,0.0,0.0,0.0])
for elemento in vet_faltas:
	vet_semana[elemento-2] = vet_semana[elemento-2] + 1
for indice in range(size(vet_semana)):
	vet_percentual[indice] = round(vet_semana[indice] * 100 / sum(vet_semana),1)
print(vet_percentual)


arte asci1
########################################################
from numpy import *
n = int(input("Informe um número:"))
cont = n
while (cont > 0):
	print("*" * cont)
	cont = cont - 1
for cont in range(1,n+1):
	print("*" * cont)
    
arte asci 2
###########################################################
from numpy import *
from math import *
n = int(input("Informe um número:"))
cont = n
while (cont > 0):
	linha = ""
	linha = linha + ("*" * cont)
	linha = linha + ("o" * abs(cont-n) * 2)
	linha = linha + ("*" * cont)
	print(linha)
	cont = cont - 1

    
  desvio padrao
  ####################################################
  from numpy import *
from math import *
vet = array(eval(input("Informe o vetor:")))
media = mean(vet)
soma = 0.0
for elemento in vet:
	soma = soma + ((elemento - media) ** 2)
dv = sqrt(soma/(size(vet)-1))
print(round(dv,3))


produtorio
############################################################
from numpy import *
from math import *
vet = array(eval(input("Informe o vetor:")))
media = mean(vet)
#print(media)
prod = 1.0
for elemento in vet:
	prod = prod * (abs(elemento - media))
p = prod ** (1/size(vet))
print(round(p,3))
#print(round(sqrt(var(vet)),3))

excluindo vogais

#############################################################

from numpy import *
texto = input("Informe texto:")
texto = texto.replace("a","")
texto = texto.replace("A","")
print(texto)
