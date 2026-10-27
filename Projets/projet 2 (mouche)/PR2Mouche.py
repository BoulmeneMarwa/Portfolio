# Créé par marwaboulmene, le 25/11/2025 en Python 3.7

# Groupe ... - Mestivier Lisa, Boulmene Marwa
# Projet L-Système

from turtle import *

#Etapes 1, 4 et 5


def remplacer1(mot,lettre,motif):
    for elem in mot:
        if lettre in mot:
            mot1 = mot.replace(lettre,motif)
    return mot1
##print(remplacer1("AdAAg", "A", "Ag"))


def itererLsysteme1(depart, regle, k):
    for k in range(0,k):
        depart = remplacer1(depart,"A", "AgAdAdAgA")
    return depart


def remplacer2(mot, lettre1, motif1, lettre2, motif2):
    mot2= ""
    for elem in mot:
        if elem == lettre1:
            mot2 += motif1
        elif elem == lettre2:
            mot2 += motif2
        else:
            mot2 += elem
    return mot2
##print(remplacer2(mot,"A", "ABg", "B", "Bd"))


def itererLsysteme2(depart, regle1, regle2, k):
    mot = ""
    for k in range(0,k):
        depart = remplacer2(depart, "A", "AgadAAgAgAAgAagAAdagAAdAdAAdAadAAA", "a", "aaaaaa")
    return depart
##print(itererLsysteme2(depart, regle1, regle2, k))


def traceLsysteme(mot, angle=90, echelle=1):
    up()
    goto(0,0)
    down()
    for elem in mot:
        if elem == "A" or elem == "B":
            fd(3)
        elif elem == "g":
            left(90)
        elif elem == "d":
            right(90)
        elif elem == "a":
            up()
            fd(3)
            down()

regle1 = ("A", "AgadAAgAgAAgAagAAdagAAdAdAAdAadAAA")
regle2= ("a","aaaaaa")
depart = "AdAdAdA"
k= 2
speed(0)
traceLsysteme(itererLsysteme2(depart, regle1, regle2,k))
exitonclick()









