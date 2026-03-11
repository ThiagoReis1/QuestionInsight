from numpy import*
alu = array(eval(input("alunos: ")))
tur = 0
for i in range(size(alu)) :
	if alu[i] % 3 == 0 :
		tur = tur + 1
print(tur)
cont = 0
a = 0
vet = zeros(tur, dtype=int)
for i in range(size(alu)) :
	if alu[i] %3 == 0 :
		vet[cont] = i
		cont = cont + 1
print(vet)
		



