var1= input("nome da armadura: ")
var2= int(input("fator de destreza: "))
if(var1 == "malha"):
	resist=15*var2 - 1
if(var1=="placas"):
	resist= 20*var2-18
print(resist)