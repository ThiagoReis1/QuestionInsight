from numpy import *

vet = array(eval(input("Numeros:")))

total = 0 

for i in range (size(vet)):
	tg = (vet[i]**(1/6))
	total = total + tg
total = (total/size(vet)) ** 6

print(round(total,2))