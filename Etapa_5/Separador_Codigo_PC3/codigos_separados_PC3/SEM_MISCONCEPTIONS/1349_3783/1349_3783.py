estimativa_de_arvores= float(input(""))
lado= float(input(""))

quantidade_de_arvores_na_regiao=  (lado**2*(25+10*(5)**(1/2))**(1/2))/4
											
quantidade_total= 	quantidade_de_arvores_na_regiao* estimativa_de_arvores							 

print(int(quantidade_total))