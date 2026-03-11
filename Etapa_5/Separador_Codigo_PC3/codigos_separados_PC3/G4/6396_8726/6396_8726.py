from numpy import* 
vit = array(eval(input("valor")))
cod = zeros(size(vit), dtype = int)


for i in range(size(vit)):
	cod[i] = vit[i] * 2  
print(cod)