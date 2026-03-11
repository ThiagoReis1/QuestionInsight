from numpy import*

codigo = array(eval(input("Digite o codigo: ")))
secret = ones(size(codigo), dtype = int)
for i in range(size(codigo)):
	secret[i] = codigo[i]**2
	
print(secret)