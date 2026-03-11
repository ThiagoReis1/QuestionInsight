p = int(input())
s = int(input())
b= int(input())

print("Entradas:", prato,",", sobre,",", bebida)
if(((p == 1) or (p == 2) or (p == 3) or (p==4))and((sobre==1)or(sobre==2)or(sobre==3)or(sobre==4))and((bebida==1)or(bebida==2)or(bebida==3)or(bebida==4))):
	if((prato == 1)and(sobre==1)and(bebida==1)):
		if(p==1):
			cal = 180
      elif(p==2):
	      cal = 230
      elif(p==3):
			cal = 250
      elif(p==4):
	      cal = 350	
				      
      if(s==1):
			cal = 75
      elif(s==2):
	      cal = 110
      elif(s==3):
	      cal = 170
      elif(s==4):
	      cal = 200	
 
      if(b==1):
			cal = 20
		elif(b==2):
	      cal = 70
      elif(b==3):
	      cal = 100
      elif(b==4):
	      cal = 65	
soma = p +s +d
print(soma)			
else:
	print("Dados invalidos")
	
