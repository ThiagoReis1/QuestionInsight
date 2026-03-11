i = int(input("idade: "))
p = float(input("peso: "))

if(i>0) and (i<=20) and (p>0) and(p<=60):
	x = "9"
	print("Grupo de risco:",x)
elif(i>0) and (i<=20) and (p>0) and (p>60) and (p<=90):
	x = "8"
	print("Grupo de risco:",x)
elif(i>0) and (i<=20) and (p>0) and (p>=90):
	x = "7"
	print("Grupo de risco:",x)
elif(i>0) and (i>20) and (i<=50) and (p>0) and (p<=60):
	x ="6"
	print("Grupo de risco:",x)
elif(i>0) and (i>20) and (i<=50) and (p>0) and (p>60) and (p<=90):
	x ="5"
	print("Grupo de risco:",x)
elif(i>0) and (i>20) and (i<=50) and (p>=90):
	x ="4"
	print("Grupo de risco:",x)
elif(i>0) and (i>50) and (p>0) and (p<=60):
	x = "3"
	print("Grupo de risco:",x)
elif(i>0) and (i>50) and (p>0) and (p>60) and (p<=90):
	x ="2"
	print("Grupo de risco:",x)
elif(i>0) and (i>50) and (p>0) and (p>90):
	x ="1"
	print("Grupo de risco:",x)
else:
	print("Dados invalidos")
	