from numpy import*

vn=array(eval(input("digite as notas")))

i=0
soma=0

while (i < size(vn)):
	soma = soma + vn[i]
	i= i + 1
	
soma=soma-min(vn)
med=soma/(size(vn)-1)

print(round(med,2))
	