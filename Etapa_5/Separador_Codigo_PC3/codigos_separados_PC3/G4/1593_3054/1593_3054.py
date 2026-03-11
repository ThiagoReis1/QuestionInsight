from numpy import*

n = array(eval(input("informe as notas: ")))
i = 0
p = 1
while(i < size(n)):
	media = (n[i] * p )#+ (n[i] *(p +1)) + (n[i] * (p+2)))/(p + (p+1) + (p + 2))
	i = i + 1
	p = p + 1
media = media / p 	
print(round(media,2))