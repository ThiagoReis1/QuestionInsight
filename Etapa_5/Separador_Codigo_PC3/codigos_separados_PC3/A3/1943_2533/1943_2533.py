#Peso Molecular do aminoácido = soma do PM de cada átomo 

#Isoleucina (C6H13NO2) #Metionina (C5H11NO2S)
#Oxigênio (O): 15.9994      #Carbono (C): 12.011
#Nitrogênio (N): 14.0067    #Enxofre (S): 32.066
#Hidrogênio (H): 1.00794

amd = input("Qual o nome do aminoácido? ").lower()
O= 15.9994
C= 12.011
N= 14.0067
S= 32.066
H= 1.00794
isoleucina = ((6*C)+(13*H)+(N)+(2*O))
metionina = ((5*C)+(11*H)+(N)+(2*O)+(S))
if(amd == "isoleucina"):
	mensagem = isoleucina
if(amd == "metionina"):
	mensagem = metionina

print(round(mensagem,2))


