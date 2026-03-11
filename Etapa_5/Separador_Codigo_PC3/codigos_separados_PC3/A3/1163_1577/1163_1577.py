p_lam= float(input("população de lambaris: "))
p_tuc= float(input("população de tucunares: "))
taxa_cl = float(input("Taxa mensal de crescimento do lambari: "))
taxa_ct = float(input("Taxa mensal de crescimento do tucunare: "))
Va_l = 0 #Variavel acumuladora
Va_t = 0 #Variavel acumuladora
i = 1  #Variavel contadora

while (p_lam != p_tuc):
	i= i+1
	Va_l = (p_lam/taxa_cl) + p_lam
	Va_t = (p_lam/taxa_ct) + p_tuc
	p_lam = Va_l - 2
	p_tuc = Va_t
	
print(i)
