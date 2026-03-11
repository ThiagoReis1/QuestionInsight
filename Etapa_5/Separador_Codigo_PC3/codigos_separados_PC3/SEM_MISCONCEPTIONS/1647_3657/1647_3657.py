from numpy import*
presenca=array(eval(input("De o vetor com as porcentagens de presenca: ")))
app=0
v=0
i=0
j=0
indice=""
while(j<size(presenca)):
	if(presenca[j]>=70):
		app=app+1
		v=v+1
		indice=indice+str(i)
	i=i+1
	j=j+1
tamanho=len(indice)
aprov=zeros(tamanho,dtype=int)
j=0
while(j<tamanho):
	aprov[j]=int(indice[j])
	j=j+1
print(app)
print(aprov)
		
