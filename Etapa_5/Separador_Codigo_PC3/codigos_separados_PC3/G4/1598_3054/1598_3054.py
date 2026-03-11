from numpy import*

c = array(eval(input("compras: ")))
d = 5
for i in range(size(c)):
	if(c[i] > 80):
		c[i] = c[i] - d
soma = sum(c)
print(round(soma,2))	
		
   			
      
	
	
