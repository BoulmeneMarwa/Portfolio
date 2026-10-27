# Créé par marwaboulmene, le 19/03/2026 en Python 3.7
import Competitor as C
import Time as T

def read_competitors(F):
    D = {}
    Lmot= []
    fichier = open(F, 'r', encoding = "utf-8")
    L= fichier.readlines()
    fichier.close()
    for i in range(1,len(L)):
        Lmot=L[i].split(";")
        Lmot[3]= Lmot[3].rstrip("\n")
        participant = C.create(Lmot[0], Lmot[1], Lmot[2], Lmot[3], i)
        D[i]= participant
    return D
##print(read_competitors("small_inscrits.csv"))

def show_competitors(competitor):
    for i in range(1,len(competitor)+1):
        print(C.to_string(competitor[i]))
##show_competitors(read_competitors("small_inscrits.csv"))

def select_competitor_by_birth_year(D, birth_date):
    MaListe = []
    for cle, val in D.items():
        if val.get("birth_date", "none").endswith(birth_date):
            MaListe.append(val)
    print(MaListe)
##select_competitor_by_birth_year(read_competitors("small_inscrits.csv"), "1980")

##def select_competitor_by_name(D,name):
##    MaListe = []
##    for cle, val in D.items():
##        if val.get("last_name", "none")== name:
##            MaListe.append(val["last_name"])
##            MaListe.append(val["first_name"])
##    print(MaListe)
##select_competitor_by_name(read_competitors("small_inscrits.csv"), "Robert")


# Fonction select_competitor_by_name(D,name) version plus courte ?
def select_competitor_by_name(D,name):
    MaListe = []
    for cle, val in D.items():
        if name in val.get("last_name",""):
            MaListe.append(val)
    return MaListe
#Fonctions suivantes (à vérifier)
def read_performances(F):
    D = {}
    fichier = open(F, 'r')
    L = fichier.readlines()
    fichier.close()
    for i in range(1,len(L)):
        ligne = L[i].split(";")
        ligne[3] = ligne[3].rstrip("\n")
        bib = int(ligne[0])
        temps = T.create(ligne[1], ligne[2], ligne[3])
        D[bib] = temps
    return D

def merge_performances(Dcomp, Dperf):
    for cle in Dperf:
        if cle in Dcomp:
            Dcomp[cle]["performance"] = Dperf[cle]
    #return
#print(merge_performances(

def sort_competitors_by_lastname(D):
    L = list(D.values())
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i]["last_name"] > L[j]["last_name"]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    return L

def sort_competitors_by_performance(D):
    L = list(D.values())
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            p1 = L[i]["performance"]
            p2 = L[j]["performance"]
            if p1 == None and p2 != None:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            elif p1 != None and p2 != None:
                if T.compare(p1, p2) > 0:
                    temp = L[i]
                    L[i] = L[j]
                    L[j] = temp
    return L
##print(sort_competitors_by_performance(merge_performances(read_competitors("small_inscrits.csv"),read_performances("small_performances"))))

def print_result_by_last_name(D):
    L = sort_competitors_by_lastname(D)
    for i in range(len(L)):
        print(C.to_string(L[i]))

def print_result_by_performance(D):
    L = sort_competitors_by_performance(D)
    for i in range(len(L)):
        if L[i]["performance"] != None:
            print(C.to_string(L[i]) + " => " + T.to_string(L[i]["performance"]))
        else:
            print(C.to_string(L[i]))

def save_results(D, fichier):
    L = sort_competitors_by_performance(D)
    f = open(fichier,"w")
    f.write("Num_dossard;Prenom;Nom;Performance\n")
    for i in range(len(L)):
        comp = L[i]
        if comp["performance"] != None:
            p = T.to_string(comp["performance"])
        else:
            p = ""
        ligne = str(comp["bib_num"]) + ";" + comp["first_name"] + ";" + comp["last_name"] + ";" + p + "\n"
        f.write(ligne)
    f.close()

D = read_competitors("small_inscrits.csv")
P = read_performances("small_performances.csv")
merge_performances(D,P)
print_result_by_performance(D)

