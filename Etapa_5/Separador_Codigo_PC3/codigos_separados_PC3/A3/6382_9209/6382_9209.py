from numpy import *

vetor_en = array(eval(input("Vetor de entrada: ")))
vetor_sa = zeros(size(vetor_en), dtype= int)
sucessor = 0


for i in range(size(vetor_en)):
	if vetor_en[i] == 9:
		vetor_sa[i] = 0
	else:
		sucessor = (vetor_en[i]+1)
		vetor_sa[i] =  vetor_sa[i]+(sucessor)**2
print(vetor_sa)