# ############ Demander l'âge    #####################
# ####################################################

from operator import ne


user_age = int(input("Entrer votre âge : "))
months = user_age * 12
days = user_age * 365

print(f"Votre âge comporte {months} mois, ou {days} jours !!!")

# ############# Les Listes #################################################################
list_names = ["Salah", "Bob", "Amar", "Kadour"]
# on ne peut pas modifier les elts dans un tuple
tuple_names = ("Salah", "Bob", "Amar", "Kadour")
set_names = {"Salah", "Bob", "Amar", "Kadour"}

list_names[1] = "Martine"
list_names = ["Salah", "Bob", "Amar", "Kadour"]
print(f"List_names devient : {list_names}")

list_names.insert(1, "Grégory")  # Insertion à la  place de Martine
print(f"List_names devient : {list_names}")

list_names.append("Khalfi")
print(f"List_names devient : {list_names}")

list_names.remove("Amar")
print(f"List_names devient : {list_names}")

list_names.pop()  # supprime le dernier elt
print(f"List_names devient : {list_names}")

list_names.pop(2)  # supprime "Bob"
print(f"List_names devient : {list_names}")

set_names.add("eric")  # l'ordre n'intervient pas dans un Set
print(f"List_names devient : {set_names}")

set_names.add("Salah")  # on peut dupliquer les elts d'un set
print(f"List_names devient : {set_names}")

# ############### Union, intersection, difference en set  ########

friends = {"Grégory", "Eric", "Ahmed", "Abdel"}
abroad = {"Amar", "Bob", "Eric"}

differ_friends = friends.difference(abroad)
print(f"La différence entre les 2 sets : {differ_friends}")

union_friends = friends.union(abroad)
print(f"L'union des 2 sets : {union_friends}")

intersec_friends = friends.intersection(abroad)
print(f"L'intersection des 2 sets : {intersec_friends}")


######################  EXERCICE  #################################
# This coding exercise requires you to complete three steps:
#
# Create a list, called my_list, with three numbers. The total of
# the numbers added together should be 100.
# Create a tuple, called my_tuple, with a single value in it
# Modify the variable set2  so that set1.intersection(set2)
# returns {5, 77, 9, 12}
# set1 = {14 , 5 , 9 , 31 , 12 , 77 , 67 , 8}
# set2 = {5}
###################################################################

# Création de la liste my_list dont la somme des elts est égale à 100

my_list = [50, 30, 20]

# Création de my_tuple avec un seul elt
my_tuple = (73, )  # Si on met (73) my_tuple ne sera pas considéré comme tuple

set1 = {14, 5, 9, 31, 12, 77, 67, 8}

# On modifie les elts de set2 pour avoir l'intersection ===> {5, 77, 9, 12}
# set2 doit contenir ses elts ci-dessous
set2 = {5, 77, 9, 12}

# Modify the variable set2  so that set1.intersection(set2)
# returns {5, 77, 9, 12}

new_set2 = set1.intersection(set2)
# l'affichage nous donne des elts non triés
print(f"Le nouveau contenu de set2 est de : {new_set2}")

# On va afficher le new_set2 avec des elts triés
# l'affichage nous donne des elts non triés
print(f"Le nouveau contenu de set2 trié est de : {sorted(new_set2)}")
