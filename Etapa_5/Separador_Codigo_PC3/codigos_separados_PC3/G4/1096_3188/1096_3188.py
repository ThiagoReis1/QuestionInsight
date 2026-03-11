#Numero fornecido (nf)
nf = int(input("Qual o numero?:"))

#Separacao de digitos1 (sd1)
sd1 = nf // 10000
#Separacao de digitos2 (sd2)
sd2 = (nf//100)%100
#Separacao de digitos3 (sd3)
sd3 = (nf%100)//1

#print(sd1,sd2,sd3)


#Formula de representatividade
soma = (sd1 ** 3)+ (sd2 ** 3) + (sd3 ** 3)

if(soma == nf):
	print("atente")
	print(nf)
else:
	print("nao atende")
	print(nf)