from numpy import*
cod = array(eval(input("Informe o codigo: ")))
n = size(cod)
i = 0
senha = zeros(n, dtype=int)
for a in cod:
	senha[i] = 2*cod[i]
	i = i + 1
print(senha)