aminoacido = input("qual o aminoacido?")
aminoacidoo = (aminoacido.lower())

o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.00794

if ( aminoacidoo != "cisteina") and ( aminoacidoo != "isoleucina") and ( aminoacidoo != "metionina"):
	print ("Entrada: " + aminoacidoo )
	print ("Dado invalido")
else:
	if ( aminoacidoo == "cisteina"):
		pesom = ( c * 3 ) + ( h * 7 ) + ( n * 1 ) + ( o * 2 ) + ( s * 1 )
		print (round(pesom,2))
	elif ( aminoacidoo == "isoleucina"):
		pesom = ( c * 6 ) + ( h * 13 ) + ( n * 1 ) + ( o * 2 )
		print (round(pesom, 2))
	elif ( aminoacidoo == "metionina"):
		pesom = ( c * 5 ) + ( h * 11 ) + ( n * 1 ) + ( o * 2 ) + ( s * 1)
		print (round(pesom,2))

	