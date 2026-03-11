from numpy import *

v = array(eval(input("")))

a = 0
mensagem = "True"

while a < size(v) - 1 :
	if v[a] > v[a+1] :
		mensagem = "False"
	a = a + 1
print(mensagem)