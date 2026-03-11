from numpy import* 
nf = array(eval(input("Notas finais dos alunos: ")))

x = 0
  
for i in range(size(nf)): 	
	if (nf[i] < 5.0): 
		x = x+1
print(x)
a = 0
cont = zeros(x, dtype=int)
for i in range (size(nf)):
	if (nf[i] < 5.0):
		cont[a] = i
		a = a+1
	
print (cont)