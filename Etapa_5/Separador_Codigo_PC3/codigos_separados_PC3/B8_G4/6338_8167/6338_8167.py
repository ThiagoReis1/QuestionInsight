from numpy import *

vet = array(eval(input("Informe os 8 elementos do vetor: ")))
num = int(input("Digite um numero: "))

i=0
acum = 0

while i<size(vet):
	if vet[i] == num:
		print(i)
	elif vet[i]>num:
		acum = acum+1
	i = i+1
	
print(acum)