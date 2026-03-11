from numpy import*

tempo= array(eval(input("tempo gasto nos banhos: ")))
percentual= array(eval(input("percentual de abertura: ")))
consumo1= (tempo*percentual)
consumo2= (consumo1/100)
consumo3= (consumo2*5)
consumo_total_agua= sum(consumo3)
print(round(consumo_total_agua, 2))