#andrea cristina de lima lopes
#matricula 20552445
# avaliacao 03

regiao=int(input())


#risco
g1=1
g2=2
g2=3
g4=4
g5=5
g6=6
g7=7
g8=8
g9=9

print("Entradas: ",(idade),"anos e",peso,"kg")
if(0>=idade and idade>= 130)or(0.0>=peso and peso>=550.0):
   print("Dados invalidos")
elif(idade<=20)and(peso<=60):
	print("Grupo de risco:",g9)
elif(idade<=20)and(60<peso<=90):
	print("Grupo de risco:",g8)
elif(idade<=20)and(peso>90):
	print("Grupo de risco:",g7)
elif(20<idade<=50)and(60<=peso):
	print("Grupo de risco:",g6)
elif(20<idade<=50)and(60<peso<=90):
	print("Grupo de risco:",g5)
elif(20<idade<=50)and(peso>90):
	print("Grupo de risco: ",g4)							
elif(50<idade)and(60<=peso):
	print("Grupo de risco: ",g3)
elif(50<idade)and(60<peso<=90):
	print("Grupo de risco: ",g2)
elif(50<idade)and(peso>90):
	print("Grupo de risco: ",g1)		