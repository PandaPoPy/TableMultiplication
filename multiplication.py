#-*- coding: utf-8 -*-
from __future__ import print_function
debut=input("Saisissez le nombre de départ:")
fin=input("Saisissez le nb de fin:")
def table(min,max):
	for i in range(min, max):
		for j in range(min, max):
			print(('%d ' % (i*j)), end='')
		#i+=1 inutile avec range()
		print('')
	#j+=1 inutile avec range()
table(debut,fin)
	
