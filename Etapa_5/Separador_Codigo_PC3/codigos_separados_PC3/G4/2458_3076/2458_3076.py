p= float(input("preco: R$ "))
cdg= int(input("COD(Regiao): "))

pcd= p*0.4
venda= (p-pcd)

cdg1= p*(10/100)
cdg2= p*(8/100)
cdg3= p*(0/100)
cdg4= p*(2/100)

if(cdg==1):
	print(round(venda+cdg1 ,2))
if(cdg==2):
	print(round(venda+cdg2 ,2))
if(cdg==3):
	print(round(venda+cdg3 ,2))
if(cdg==4):
	print(round(venda+cdg4 ,2))