from numpy import*

seq= array(eval(input("Insira o codigo: ")))

for i in range(size(seq)):
	if seq[i] == 9:
		seq[i] = 0
	else:
		seq[i]= (seq[i] + 1) **2
	
print(seq)