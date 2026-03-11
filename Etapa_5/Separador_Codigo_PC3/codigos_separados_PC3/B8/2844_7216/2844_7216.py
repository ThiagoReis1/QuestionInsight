from numpy import*

codigo = array(eval(input("")))
mensagem = zeros(size(codigo), dtype = int)
				
for i in range(size(codigo)):
	if codigo[i] !=0:
		mensagem[i] = codigo[i] - 1		
	elif codigo[i] == 0:
		mensagem[i] = 9
					
print(mensagem)
								  