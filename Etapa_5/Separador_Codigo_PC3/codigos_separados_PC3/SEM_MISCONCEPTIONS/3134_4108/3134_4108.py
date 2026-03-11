from numpy import*
v= array(eval(input("Numeros: ")))
i = 0
n = size(v)
soma = zeros(n,dtype = float)

while i < size(v):
	soma[i] = v[i]*v[i]
	numerador = sum(soma)
	
	media = (numerador/n)**0.5
	i = i+ 1
print(round(media,2))

	