arma = input("digite o nome da arma: ") 
fator = int(input("digite o fator de sucesso"))  

machado = 30 * (fator/10)
lanca = 5 + 20 * (fator/10) 

if(arma == "machado"):
   print int((machado))
else:
   print int((lanca))  


 