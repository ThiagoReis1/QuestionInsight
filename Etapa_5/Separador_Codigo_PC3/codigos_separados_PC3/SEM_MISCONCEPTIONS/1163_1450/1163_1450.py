# Universidade Federal do Amazonas
# Aluna: Karina Rocha Ferreira - 21554907
# Av.4 
# 27/07/2016

print("Numero de lambaris: ")
ilamb = int(input())

print("Numero de tucunares: ")
itucu = int(input())

print("Taxa de lambaris: ")
taxa_lamb = float(input())

print("Taxa de tucunares: ")
taxa_tucu = float(input())

n_lamb = ilamb * taxa_lamb
n_tucu = itucu * taxa_tucu
acum_lamb = n_lamb
acum_tucu = n_tucu
meses = 0
while (acum_lamb == acum_tucu):
	meses = meses + 1
	acum_lamb = n_lamb - (2 * n_tucu
	acum_tucu = n_tucu 
	
	
print(meses)