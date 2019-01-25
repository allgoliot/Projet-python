# Opération sur les fichiers 
#créer (collaboration avec les sous-repertoires suivants)
# developpements, tests, livraisons, bugs
import os
import os.path
def fichiers():
	chemin = "./collaboration"
	sous_rep = ["developpements", "tests", "livraisons", "bugs"]
	if not os.path.exists(chemin):
		os.makedirs (chemin)
		for i in sous_rep:
			os.makedirs (chemin+"/"+i)
fichiers()