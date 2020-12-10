
import sys
import threading
from queue import *
import random
import time
from threading import *


#initialisation d'une file
BUF_SIZE = 30
Stock = Queue(BUF_SIZE)
#création de la class Producer
class Producer(Thread):
	def __init__(self):
		self.can_produce = True
		Thread.__init__(self)
	#Méthode wait() qui permet de faire les time.sleep()
	def wait(self):
		time.sleep(random.uniform(0, 3))

	#Méthode produce_item permet de remplir la file Stock.
	def produce_item(self):
		#Tant que le producteur peut produire des iphone_12
		while self.can_produce:
			#et Tant que la file n'est pas remplie
			while not Stock.full():

				try:
					prod_num = random.randint(1,5)
					### le Producteur va ajouter un iphone_12 dans la vitrine, et s'il y a plus de place,
					Stock.put("ajout d'un iphone_12", True, 10)
					### va attendre pendant 1 seconde qu'un iphone_12 soit achete.
				except Full as e:
					print("Il n'y a pas de place pour un iphone_12 !\n");

				else:
					print("Le producteur "+str(prod_num) + " ajoute un iphone_12 dans la vitrine, il y a ", str(Stock.qsize()), "iphone_12")

			self.wait()

	#Méthode run qui permet de lancer la fonction produce_item
	def run(self):
		self.produce_item()


#création de la classe Consumer qui contient deux attributs :le produit(items) et numéro du consomateur(numero).
class Consumer(Thread):
	def __init__(self, need, numero):
		self.need = need
		self.numero = numero
		Thread.__init__(self)

	def wait(self):
		time.sleep(random.uniform(0, 3))

	def consume_item(self):
		#Tant que items = True (le produit est disponible)
		while self.need == True:

			self.wait()
			okey = False
			# nombres de iphone_12 qu'il va prendre ( valeur aléatoire entre 1 et 10)
			paquet = random.randint(1, 3)

			#On initialise une variable i à 1
			i = 1
			print("Le client " + str(self.numero) + " veut " + str(paquet) + " iphone_12")
			#tant que i est <= au nombre d'iphones demandé pa le client
			while i <= paquet:
				#on retire un iphone_12(element) dans la file
				try:
					Stock.get(True,None)
					#on crée un booléen okey vaut True
					okey = True
					print("Le client " + str(self.numero) + ": Prend un iphone_12")

				except Empty as e:
					okey = False
					break
				else:
					i += 1
			#une fois que le client a pris le nombre de Iphone_12 qu'il veut, on affiche le nombre de iphone_12 qui reste dans la vitrine.
			if okey:
				print("Il reste  " + str(Stock.qsize()) + " iphone_12\n")

			#sinon le client va dire qu'il n ya pas assez de iphnoe_12 dans la vitrine.
			else:
				print("n " + str(self.numero) + ": Il n ya pas assez de smartphone iphone_12 dans la vitrine")
			self.need = False

	def run(self):
		self.consume_item()

if __name__ == "__main__":

	p = Producer()
	p.can_produce = True
	print("_____ Bienvenue au magasin de smartphones _____\n")
	p.start()
	n = random.randint(10,30)
	i=1
	while i < n:
		c= Consumer(need=True, numero=i)
		c.start()
		i = i + 1
	time.sleep(10)

	p.can_produce = False
	print("_____ Le magasin est fermé, à bientôt _____\n")

