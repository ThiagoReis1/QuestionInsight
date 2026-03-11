numero= int(input("qual valor: "))
n01= numero // 100
resto_n01= numero%100
n02=resto_n01//1
form =(n01+n02)**2
if(form == numero):
	texto=("atende")
else:
	texto=("nao atende")
print(numero)
print(texto)