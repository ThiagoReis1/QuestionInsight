from numpy import *
#formula do dano total:dm = s[i]*n[1]
#gelo=2
#fogo=3
#choque=4
#conjuração=8
#ilusão=10
s = array(eval(input("Magia: ")))
n = array(eval(input("Mago: ")))


i=0
dm=0
g=2 #gelo
f=3 #fogo
ch=4 #choque
c=8 #conjuração
l=10 #ilusão
while(i<size(s)):
	if(s[i]=="GELO"):
		dm = dm + (g*n[i])
	elif(s[i]=="FOGO"):
		dm = dm + (f*n[i])
	elif(s[i]=="CHOQUE"):
		dm = dm + (ch*n[i])
	elif(s[i]=="CONJURACAO"):
		dm = dm + (c*n[i])
	elif(s[i]=="ILUSAO"):
		dm = dm + (l*n[i])
	i=i+1
print(dm)