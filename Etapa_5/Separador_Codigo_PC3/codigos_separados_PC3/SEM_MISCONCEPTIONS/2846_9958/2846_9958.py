from numpy import *

mensagem = array(eval(input("msg")))

cifrada = zeros(size(mensagem),dtype=int)

for i in range(size(mensagem)):
	cifrada[i]=2*mensagem[i]
print(cifrada)
