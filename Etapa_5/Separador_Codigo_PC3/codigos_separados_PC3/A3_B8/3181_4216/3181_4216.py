from numpy import*

v = array(eval(input("No jogadas: ")))
quadro = zeros(size(v), dtype=int)

zero = 0
um = 0
dois = 0
tres = 0
quatro = 0
cinco = 0
seis = 0
sete = 0 
oito = 0
nove = 0
dez = 0
onze = 0
doze = 0
treze = 0
catorze = 0
quinze = 0
dezesseis = 0
dezessete = 0
dezoito = 0
dezenove = 0
vinte = 0
vum = 0
vdois = 0
vtres = 0
vquatro = 0
vcinzo = 0
vseis = 0
vsete = 0
voito = 0
vnove = 0
trinta = 0 
taum = 0
tdois = 0
ttres = 0
tquatro = 0
tcinco = 0
tseis = 0
#
for i in range(size(v)):
	if(v[i]==0):
		zero = zero + 1
	elif(v[i])==1:
		um = um + 1
	elif(v[i]==2):
		dois = dois + 1
	elif(v[i]==3):
		tres = tres + 1
	elif(v[i]==4):
		quatro = quatro + 1
	elif(v[i]==5):
		cinco = cinco + 1
	elif(v[i]==6):
		seis = seis + 1
	elif(v[i]==7):
		sete = sete + 1
	elif(v[i]==8):
		oito = oito + 1
	elif(v[i]==9):
		nove = nove + 1
	elif(v[i]==10):
		dez= dez + 1
		
	elif(v[i]==11):
		onze = onze + 1
	elif(v[i]==12):
		doze = doze + 1
	elif(v[i]==13):
		treze = treze + 1
	elif(v[i]==14):
		catorze = catorze + 1
	elif(v[i]==15):
		quinze = quinze + 1
	elif(v[i]==16):
		dezesseis = dezesseis + 1
	elif(v[i]==17):
		dezessete  = dezessete + 1
	elif(v[i]==18):
		dezoito = dezoito + 1
	elif(v[i]==19):
		dezenove = dezenove + 1
	elif(v[i]==20):
		vinte = vinte + 1
	elif(v[i]==21):
		vum = vinteum + 1
	elif(v[i]==22):
		vdois = vdois + 1
	elif(v[i]==23):
		vtres = vtres + 1
	elif(v[i]==24):
		vquatro = vquatro + 1
	elif(v[i]==25):
		vcinco = vcinco + 1
	elif(v[i]==26):
		vseis = vseis + 1
	elif(v[i]==27):
		vsete = vsete + 1
	elif(v[i]==28):
		voito = voito + 1
	elif(v[i]==29):
		vnove = vnove + 1
	elif(v[i]==30):
		trinta = trinta + 1
	elif(v[i]==31):
		tum = tum + 1
	elif(v[i]==32):
		tdois = tdois + 1
	elif(v[i]==33):
		ttres = tres + 1
	elif(v[i]==34):
		tquatro = tquatro +1
	elif(v[i]==35):
		tcinco = tcinco + 1
	elif(v[i]==36):
		tseis = tseis + 1
quadro[0]=zero
quadro[1]=um
quadro[2]=dois
quadro[3]=tres
quadro[4]=quatro
quadro[5]=cinco
quadro[6]=seis
quadro[7]=sete
quadro[8]=oito
quadro[9]=nove
quadro[10]=dez
quadro[11]=onde
quadro[12]=doze
quadro[13]=treze
quadro[14]=catorze
quadro[15]=quinze
quadro[16]=dezesseis
quadro[17]=dezessete
quadro[18]=dezoito
quadro[19]=dezenove
quadro[20]=vinte
quadro[21]=vum
quadro[22]=vdois
quadro[23]=vtres
quadro[24]=vquatro
quadro[25]=vcinco
quadro[26]=vseis
quadro[27]=vsete
quadro[28]=voito
quadro[29]=vnove
quadro[30]=trinta
quadro[31]=tum
quadro[32]=tdois
quadro[33]=ttres
quadro[34]=tquatro
quadro[35]=tcinco
quadro[36]=tseis

print(quadro)