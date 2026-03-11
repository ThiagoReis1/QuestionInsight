#variavel 
ps = float ( input ("Peso do saco de racao: "))
qtd = float ( input ("Quantidade diaria: "))


#corpo
c = ( qtd * 4 )
qr = ps - c


#mostrador
print ( round( qr , 2 ))