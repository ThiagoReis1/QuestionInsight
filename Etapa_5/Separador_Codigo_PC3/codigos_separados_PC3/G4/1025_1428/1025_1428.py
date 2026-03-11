#Universidade Federal Do Amazonas	
# Mary jane Dos Santos Venancio-21453516	

#largura do terreno da fazenda
A = float(input("digite a largura do terreno: "))
#comprimento do terreno da fazenda
a = float(input("digite o comprimento do terreno:"))
#custo de produção
c_p = float(input("digite o custo da produção:"))

custo_total = ((2 * (A + a)) * c_p)
print (round(custo_total,2))