from numpy import*
cod = array(eval(input("coloque o codigo : ")))
cod_new = zeros(size(cod), dtype = "int")
for i in range(size(cod)):
	if cod [i] == 0 :
		cod_new [i] = 9 ** 3
	else:
		cod_new [i] = (cod [i] -1) **3
print(cod_new)
