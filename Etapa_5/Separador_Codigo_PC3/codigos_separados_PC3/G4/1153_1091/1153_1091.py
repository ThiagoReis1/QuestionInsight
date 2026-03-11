p_P= float(input("Digite o patrimonio em dolares: "))
p_B= float(input("Digite o patrimonio em dolares: "))
c_P= float(input("Digite o percentual de crescimento: "))
c_B= float(input("Digite o percentual de crescimeneto:"))
i=1
while (p_B<p_P):
	i=i+1
	p_P=p_P+p_P*(c_P/100)
	p_B=p_B+p_B*(c_B/100)
print (i)
	
	
