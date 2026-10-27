# Créé par marwaboulmene, le 17/03/2026 en Python 3.7

def create(hours, minutes, seconds):
    T = {}
    T["h"] = int(hours)
    T["m"] = int(minutes)
    T["s"] = int(seconds)
    return T


def heure(t):
    return t["h"]


def minutes(t):
    return t["m"]


def seconds(t):
    return t["s"]


def to_seconds(t):
    return t["h"]*3600 + t["m"]*60 + t["s"]


def compare(t1, t2):
    return to_seconds(t1) - to_seconds(t2)


def to_string(t):
    return str(t["h"]) + "h" + str(t["m"]) + "mn" + str(t["s"]) + "s"