# Créé par marwaboulmene, le 23/09/2025 en Python 3.7
# Groupe Tulipes – Bernard Tom, Boulmene Marwa
# Projet n°1 – Bouquet de polygones

from turtle import *
from random import randint

def dessinePoly():
    '''fonction qui dessine un polygone en fonction du nombre de côtés aléatoire, de leur longueur et de leur angles'''
    nb_cotes = randint (3,6)
    long = 50
    angle = 360/nb_cotes
    down ()
    for i in range (nb_cotes):
        fd (long)
        left(angle)




def dessineFleur():
    '''fonction qui dessine des fleurs, ayant une couleur aléatoire et un penthagone blanc afin que seuls les triangles de celle-ci soient colorés '''
    color((randint(0,255),randint(0,255), randint(0,255)))
    begin_fill()
    for i in range(5):
        fd (50)
        left (144)
    end_fill()
    color(173,216,230)
    begin_fill()
    up()
    fd(19)
    down()
    for i in range (5):
        fd(12)
        left(360/5)
    up()
    bk(19)
    down()
    end_fill()


def dessineTige(n):
    '''fonction qui dessine les tiges du bouquet en prenant en compte la distance recurrente entre deux tiges différentes, leur epaisseur aléatoire, et ayant soit un polygone soit une fleur au bout (colorés) '''
    color(0,100,0)
    width(randint(1,5))
    d_tige = 180/(n+3)
    l_tige = randint(50,350)
    fd(l_tige)
    a = randint(0,1)
    if a == 0 :
        dessineFleur()
    else :
        color((randint(0,255),randint(0,255), randint(0,255)))
        begin_fill()
        dessinePoly()
        end_fill()
    color(0,100,0)
    backward(l_tige)
    left(d_tige)

def dessineBouquet(n):
    '''fonction qui assemble les programmes dessineTige (qui contient dessineFleur et dessinePoly) afin de créer le bouquet de fleurs'''
    setup(900,600)
    bgcolor(173,216,230)
    hideturtle()
    up()
    goto(-300,190)
    down()
    color("yellow")
    begin_fill()
    circle(50)
    end_fill()
    up()
    goto(0,-150)
    down()
    d_tige = 180/(n+3)
    speed(3)
    left(d_tige* 2)
    for j in range (n):
        dessineTige(n)



colormode(255)
speed(6)
dessineBouquet(10)
exitonclick()


