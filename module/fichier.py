# Opération sur les fichiers 
#créer (collaboration avec les sous-repertoires suivants)
# developpements, tests, livraisons, bugs
#Puis créer respectivement dans chaque sous repertoire les fichiers suivants: 
#developpement.txt, tests.txt, livraisons.txt et bugs.txt
#dans developpements.txt, écrire la phrase: ce repertoire contiendra vos développements
#dans tests.txt, écrire la phrase: ce repertoire contiendra vos tests
#dans livraisons.txt, écrire la phrase: ce repertoire contiendra vos livraisons
#dans bugs.txt, écrire la phrase: ce repertoire contiendra les bugs rencontrés
import os
import os.path
def fichiers():
	chemin = "./collaboration"
	sous_rep = ["developpements", "tests", "livraisons", "bugs"]
	if not os.path.exists(chemin):
		os.makedirs (chemin)
		for i in sous_rep:
			os.makedirs (chemin+"/"+i)
			source = chemin+"/"+i+"/"+i+".txt"
			fichiers = open(source, "w")
			fichiers.write("ce repertoire contiendra vos " + i)
			fichiers.close()
		
fichiers()