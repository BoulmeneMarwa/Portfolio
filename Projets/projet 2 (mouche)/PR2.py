# Créé par marwaboulmene, le 25/11/2025 en Python 3.7

# Groupe Mouche - Mestivier Lisa, Boulmene Marwa
# Projet L-Système

from turtle import *

#Etapes 1, 4 et 5:
"""fonction qui trace un dessin a partir d'un mot"""
def traceLsysteme(mot, angle, echelle):
    liste = []
    element = []
    for elem in mot:
        if elem == "A" or elem == "B":
            """ si la lettre lu est un A ou un B, faire l'instruction suivante"""
            fd(10*echelle)
        elif elem == "g":
            """ si la lettre lu est un g, faire l'instruction suivante"""
            left(angle)
        elif elem == "d":
            """ si la lettre lu est un d, faire l'instruction suivante"""
            right(angle)
        elif elem == "a":
            up()
            fd(10*echelle)
            down()
        elif elem == "[":
            up()
            liste.append(heading())
            liste.append(position())
            down()
        elif elem == "]":
            up()
            element = liste.pop()
            goto((int(element[0])), int(element[1]))
            element = liste.pop()
            setheading(int(element))
            down()



#etape 2:
def remplacer1(mot,lettre,motif):
    """fonction qui remplace une lettre par un motif dans un mot"""
    for elem in mot:
        if elem== lettre:
            mot1 = mot.replace(lettre,motif)
    return mot1



def itererLsysteme1(depart, regle, k):
    """fonction qui calcule le k-eme itéré du L-Systeme associé au mot initial"""
    for k in range(0,k):
        depart = remplacer1(depart,regle[0], regle[1])
    return depart


def remplacer2(mot, lettre1, motif1, lettre2, motif2):
    """fonction qui remplace une lettre par un motif dans un mot """
    mot2= ""
    for elem in mot:
        if elem == lettre1:
            mot2 += motif1
        elif elem == lettre2:
            mot2 += motif2
        else:
            mot2 += elem
    return mot2



def itererLsysteme2(depart, regle1, regle2, k):
    """fonction qui calcule le k-eme itéré du L-Systeme associé au mot initial"""
    for k in range(0,k):
        depart = remplacer2(depart, regle1[0], regle1[1], regle2[0], regle2[1])
    return depart


def dessin(numEtape):
    """ dessine le dessin de l'étape nimEtape"""
    speed(-10)
    #Etape1:
    if numEtape == 1:
        bgcolor("light blue")
        color("orange")
        motEtape1 = "AgAdAAdAdA"
        up(), goto(-100,0), down()
        traceLsysteme(motEtape1,90,10)
    #Etape2:
    elif numEtape == 2:
        bgcolor("red")
        color("light green")
        regle = ("A", "AgAdAdAgA")
        depart = "A"
        k=4
        up(), goto(-200,0), down()
        traceLsysteme(itererLsysteme1(depart,regle,k), 90, 0.5)
    #Etape3:
    elif numEtape == 3:
        bgcolor("green")
        color("pink")
        motEtape3= "AdBdB"
        regle1 =("A", "AdBgAgBdA")
        regle2= ("B", "BB")
        k= 4
        up(), goto(-100,0), down()
        traceLsysteme(itererLsysteme2(motEtape3, regle1, regle2, k), -120 ,1)
    #Etape4:
    elif numEtape == 4:
        bgcolor("dark blue")
        color("light blue")
        motEtape4 = "AdAdAdA"
        regle1= ("A", "AgadAAgAgAAgAagAAdagAAdAdAAdAadAAA")
        regle2=("a","aaaaaa")
        k= 4
        up(), goto(-90,100), down()
        traceLsysteme(itererLsysteme2(motEtape4, regle1, regle2, k), 90 ,0.4)
    #Etape5:
    elif numEtape == 5:
        bgcolor("light blue")
        color("dark blue")
        motEtape5 = "A"
        regle1= ("A","A[gA]A[dA]A")
        k= 3
        setheading(90)
        up(), goto(0,-200), down()
        traceLsysteme(itererLsysteme1(motEtape5, regle1, k), 25 ,1)
    hideturtle()
    exitonclick()
#dessin(1)
#dessin(2)
#dessin(3)
#dessin(4)
dessin(5)

exitonclick()









