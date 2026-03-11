from numpy import*
vet1 =  array(eval(input("digite nmr de aneis de 1:")))
vet2 =  array(eval(input("digite nmr de aneis de 2:")))
i = 0
anel1 = 0
anel2 = 0
while(i<size(vet1)and (i<size(vet2))):
	if(vet1[i]==1):
		anel1 =  anel1 + 40
	if(vet2[i]==1):
		anel2 = anel2 + 40
	if(vet1[i]==2) :
		anel1= anel1 + 20 
	if(vet2[i]==2):
		anel2=  anel2 + 20
	if(vet1[i]==3):
		anel1 =  anel1 + 20
	if(vet2[i] == 3):
		anel2 = anel2 + 10
	if(vet1[i]>=4):
		anel1 = anel1 + 0
	if(vet2[i]>=4):
		anel2 = anel2 + 0
	i = i + 1
if(sum(anel1)>sum(anel2)):
	print("JOGADOR UM")
if(sum(anel1)<sum(anel2)):
	print("JOGADOR DOIS")
if(sum(anel1) == sum(anel2)):
	print("EMPATE")