#leitura dos dados
peso= float(input("digite o valor do produto:"))
distancia= float(input("digite a distancia:"))
codigo= int(input("digite o codigo:"))
custo= peso*25.00
custo2= distancia*0.10
if(codigo==1):
	servico=((custo)+(custo2))*(1+(17/100))
elif(codigo==2):
	servico= ((custo)+(custo2))*(1+ (17.5/100))
elif(codigo==3):
	servico= ((custo)+(custo2))*(1+(18/100))
else:
	servico= ((custo)+(custo2))*(1+(20/100))
print(round(servico, 2))
