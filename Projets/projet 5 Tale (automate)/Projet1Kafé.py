# Créé par marwaboulmene, le 15/09/2026 en Python 3.7

# Groupe Kafé - BOULMENE Marwa, LELAURIN Tom
# Projet n°1 : Les automatismes finis non déterministes

def creerAutomate (fichier):
    f = open(fichier, mode = "r", encoding = "utf-8")
    EFinaux = f.readline().split()
    automate = []
    ligne = []
    for elem in f:
        ligne.append(elem.split())

    for i in range(len(ligne)):
        val = int(ligne[i][0])
        while len(automate) <= val:
            automate.append([])

    for elem in ligne:
        automate[int(elem[0])].append((elem[1],elem[2]))
    f.close()
    return automate, EFinaux

print(creerAutomate("automate.txt"))
# On souhaite [[('a','1'),('b','1')('a','2')],[...]]

def testMot(mot,fichier):
    automate, Efinaux = creerAutomate(fichier)
    SEtat = {0}
    for elem in mot:
        SNewEtat = set()
        for val in SEtat:
            for item in automate[val]:
                if item[0] == elem:
                    SNewEtat.add(int(item[1]))
        SEtat = SNewEtat.copy()
    for val in SEtat:
        if str(val) in Efinaux:
            return True
    return False



print(testMot('abc', "automate.txt")) #On souhaite avoir "True"
print(testMot('abcd', "automate.txt"))#On souhaite avoir "True"
print(testMot('bacd', "automate.txt")) #On souhaite avoir "False"
print(testMot('cdb', "automate.txt")) #On souhaite avoir "False"
print(testMot('abcc', "automate.txt")) #On souhaite avoir "False"
