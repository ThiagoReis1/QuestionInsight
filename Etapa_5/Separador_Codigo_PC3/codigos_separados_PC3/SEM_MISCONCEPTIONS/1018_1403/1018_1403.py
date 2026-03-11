cateto_a= float(input("digite o valor: "))
cateto_b= float(input("digite o valor: "))
custo_de_aplicacao_por_m2= float(input("digite o valor:"))
area= (cateto_a*cateto_b)/2
custo_total= area*custo_de_aplicacao_por_m2
print (round(custo_total,2))
