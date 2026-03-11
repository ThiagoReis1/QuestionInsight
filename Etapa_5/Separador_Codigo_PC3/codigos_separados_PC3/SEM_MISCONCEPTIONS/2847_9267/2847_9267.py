from numpy import*

codigo = array(eval(input('Digite o codigo: ')))
codigo_new = zeros(size(codigo), dtype=int)

for i in range(size(codigo)):
	codigo_new[i]=codigo[i]*codigo[i]
print(codigo_new)