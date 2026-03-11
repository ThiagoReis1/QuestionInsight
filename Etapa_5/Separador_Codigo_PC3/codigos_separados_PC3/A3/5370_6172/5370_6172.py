from numpy import*

v = array(eval(input()))
i = 0
mensagem = "True"

while i < size(v) - 1:
	if v[i] >  v[i + 1]:
		mensagem = "False"
	i = i + 1
print(mensagem)
		
