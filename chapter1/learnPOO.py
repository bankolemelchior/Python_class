class vehicule:
  """
  Voici un exemple de classe "vehicule" qui contient le plan de conception
  d'objets "véhicules"
  """

  # Une classe commence par une fonction initialisation qui contient les différents attributs
  def __init__(self, couleur='noire', vitesse=0, roues=4):
    self.couleur = couleur
    self.vitesse = vitesse
    self.roues = roues
    
  # voici une méthode "accelerer" qui modifie un attribut de l'objet
  def accelerer(self, vitesse):
    self.vitesse += vitesse

  # voici une autre méthode
  def stop(self):
    self.vitesse = 0

  # voici une derniere méthode, tres souvent utilisée
  def afficher(self):
    print(f'couleur: {self.couleur}\nroues: {self.roues}\nvitesse: {self.vitesse}')


class voiture_electrique(vehicule):
  """
  La classe moto hérite des méthodes et des attributs de la classe véhicule
  """

  def __init__(self, couleur='black', vitesse=0, roues=4, autonomie=100):
    super().__init__(couleur, vitesse, roues) # super() permet d'utiliser la fonction de la classe "parent"
    self.autonomie = autonomie

  # Ré-écriture de certaines méthodes
  def accelerer(self, vitesse):
    super().accelerer(vitesse)
    self.autonomie -= 0.1 *self.vitesse

  def afficher(self):
    super().afficher()
    print(f'autonomie: {self.autonomie}')
yaris=vehicule('bleue',10,4)
yaris.accelerer(100)
yaris.afficher()

zoe=voiture_electrique('blanche')
zoe.accelerer(140)
zoe.afficher()