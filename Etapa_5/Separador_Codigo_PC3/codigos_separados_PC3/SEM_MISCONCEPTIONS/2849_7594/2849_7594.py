from numpy import*

v_num = array(eval(input("Vetor numerico: ")))
soma = 0 

for i in range(size(v_num)):
	soma += v_num [i]
	if v_num[i] == 0:
		soma = 0
		
print(soma)
		