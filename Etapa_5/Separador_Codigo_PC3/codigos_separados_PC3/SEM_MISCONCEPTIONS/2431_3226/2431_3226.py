precocliente=float(input())
precoacompanhante=float(input())
taxadesconto=0.35
desconto=precoacompanhante - (precoacompanhante*(taxadesconto))
precototal=precocliente + desconto
print(round(precocliente,2))
print(round(desconto,2))
print(round(precototal,2))						 
