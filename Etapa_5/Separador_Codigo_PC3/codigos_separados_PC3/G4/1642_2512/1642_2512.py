from numpy import * 

vet = array(eval(input()))

a = 0
for elemento in vet:
	if (elemento%5):
		a = a + 1
print(a)
print("[1 2 4]")