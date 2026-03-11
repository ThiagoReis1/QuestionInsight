i=int(input("idade:"))
p=float(input("peso:"))	
if(i<0)or(i>130)or(p<0.0)or(p>550.0):
	print("Dados invalidos")
elif(i<=20)and(p<=60.0):
	print("Grupo de risco: 9")
elif(i<=20)and(p>60.0)and(p<=90.0):
	print("Grupo de risco: 8")
elif(i<=20)and(p>90.0):
	print("Grupo de risco: 7")
elif(i>20)and(i<=50)and(p<=60.0):
   print("Grupo de risco: 6")
elif(i>20)and(i<=50)and(p>60.0)and(p<=90.0):
   print("Grupo de risco: 5")
elif(i>20)and(i<=50)and(p>90.0):
	print("Grupo de risco: 4")
elif(i>50)and(p<=60.0):
	print("Grupo de risco: 3")
elif(i>50)and(p>60.0)and(p<=90.0):
	print("Grupo de risco: 2")
elif(i>50)and(p>60.0)and(p>90.0):
	print("Grupo de risco: 1")
