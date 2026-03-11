from numpy import*

an = array(eval(input()) ,dtype=int)
cont = 0

for i in an:
   if(i == 1):
	   cont += 80
		
   elif(i == 2):
	   cont += 40
	
   elif(i == 3):
      cont += 20
	
   elif(i == 4):
      cont += 10

print(cont)