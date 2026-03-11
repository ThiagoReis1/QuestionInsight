from numpy import*

quant = array(eval(input("Saques efetuados: "))) 

cont  = 0
entrada = 0 



for x in range(size(quant)):
	if quant[x] <= 50:
		cont = cont +1
		resultado = cont 
i = zeros(cont, dtype=int)

for x in range(size(quant)):
	if quant[x] <= 50:
		i[entrada] = x 
		entrada = entrada + 1 

print(cont)
print(i)



