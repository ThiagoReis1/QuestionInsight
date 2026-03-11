#---------------------------------------------------------
#UNIVERSIDADE FEDERAL DO AMAZONAS 	
#VICTHORYA STHEFFANNY GOMES LIRA
#DATA:30/06/2016
#OBJETIVO: IMPLEMENTAR DECISÕES USANDO O COMANDO IF E ELSE  
#----------------------------------------------------------
p1= float(input("digite a nota: "))		
p2= float(input("digite a nota: "))	
p3= float(input("digite a nota: "))	
p4= float(input("digite a nota: "))	
nt=(p1+p2+p3+p4)/4

if(nt >=6):
	print(round(nt,1))
	print("Aprovado")

else:
	print(round(nt,1))
	print("Reprovado")
