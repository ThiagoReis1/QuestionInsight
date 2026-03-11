num = int(input("Digite um numero: "))
inicial = 0

soma = 0
sinal = +1

while(num!=0):
	soma = soma + num
	num = int(input("Digite um numero: "))
	inicial = 0
	if(soma<0) and (soma!=0):
		mensagem = "Esquerda"
	if(soma>0):
		mensagem = "Direita"
	if(soma==0):
		mensagem = "Inicial"
		

	
print(soma)
print(mensagem)
	