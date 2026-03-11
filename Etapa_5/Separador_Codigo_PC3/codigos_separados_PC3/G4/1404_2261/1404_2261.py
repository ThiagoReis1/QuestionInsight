ndc = input("nome da cabeça:")

#dados
d1 = int(input("valores do dado 1:"))
d2 = int(input("valores do dado 2:"))
d3 = int(input("valores do dado 3:"))

if(ndc.lower()=="aameul"):
	dano = 8 + (d1+d2+d3)
else:
	dano =  (d1+d2+d3)*2
print(dano)