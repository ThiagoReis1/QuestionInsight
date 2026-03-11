from numpy import*
n = array(eval(input()))
menor = 999999
linhas= n.shape[0]
for i in range(linhas):
	mn = min(n[i,:])
	if(menor > mn):
		menor = mn
print(mn)
