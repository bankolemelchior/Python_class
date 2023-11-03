"""
x = 5;
y = 15;

print('x + y =', x + y)
print('x - y =', x - y)
print('x / y =', x / y)
print('x // y =', x // y) # division entiere (tres utile pour les tableaux Numpy)
print('x  y =', x * y)
print('x ^ y =', x ** y) # x puissance y

print('égalité :', x == y)
print('inégalité :', x != y)
print('inférieur ou égal :', x <= y)
print('supérieur ou égal :', x >= y)

^ le ou exclisif
"""

# def userName(lnam, fname):
#     return lnam, fname;
#     # print("Votre nom est " + lnam + " et votre prénom est " + fname );
    
# getInfo = userName("Bravo", "Mike");
# print(getInfo);

"""
#Energie potentiel
def e_potentielle(masse, hauteur, energie_limite, g=9.81):
  energie = masse  hauteur  g 
  print(energie)
  return energie > energie_limite

# ici g a une valeur par défaut donc nous ne sommes pas obligé de lui donner une valeur
e_potentielle(masse=10, hauteur=10,energie_limite=1000)

def e_potentielle(masse, hauteur, limite, g=9.81): exo avec les structures de contrôle
    energie = masse * hauteur * g
    if energie > limite:
        return "l'énergit calculée est supérieure à la limite"
    else:
        return energie
energie_info = e_potentielle(1, 2, 30);
print(energie_info);

"""
#range(start, stop(exclusif), step)
# for i in range(0, 10, 2):
#     print(i);


def fibonacci(n):
    a,b = 0, 1
    while b < n:
        c = a + b
        a,b = b,c
        print(a)
fibonacci(10)

"""
villes = ['Paris', 'Berlin', 'Londres', 'Bruxelles'] # liste initiale
print(villes)

villes.append('Dublin') # Rajoute un élément a la fin de la liste
print(villes)

villes.insert(2, 'Madrid') # Rajoute un élément a l'index indiqué
print(villes)

villes.extend(['Amsterdam', 'Rome']) # Rajoute une liste a la fin de notre liste
print(villes)

print('longeur de la liste:', len(villes)) #affiche la longueur de la liste

villes.sort(reverse=False) # trie la liste par ordre alphabétique / numérique
print(villes)

print(villes.count('Paris')) # compte le nombre de fois qu'un élément apparait dans la liste
"""