from module.listes import *
from module.geometrie import *
from module.mathematiques import *
from module.fichier import *

def menutotal():
	fin=0
	while fin == 0:
		print("Menu des py")
		print("1. Geometrie")
		print("2. Listes")
		print("3. Math")
		print("4. Fichier")
		print("*. Sortie")
		choix=input("Votre choix : ")
		
		if choix=="1": #geometrie
			menugeo()
		elif choix=="2":#listes
			menuliste()
		elif choix=="3":#math
			demomath()
		elif choix=="4": #fichier
			fichier()
		else:
			print("Aucun choix")
			print("Fin du programme")
			fin = 1

menutotal()