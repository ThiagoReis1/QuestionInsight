valor = int(input("A"))

n01=valor//10000
resto_n01 = valor%10000
n02= resto_n01//100
resto_n02=resto_n01%100
n03=resto_n02//1

calc=(n01**3)+(n02**3)+(n03**3)

if (calc==valor):
   texto=("atende")
else:
	texto=("nao atende")

print(texto)
print(valor)
    