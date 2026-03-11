var = int(input("Digite um numero: "))
if(var <= 9999 and var >=1000):
	
   first_quad = var//100 
   second_quad = var%100

   prop = first_quad**2 + second_quad**2 

   if(var == prop):
	   print(var,"atende a propriedade")
   else:
	   print(prop)