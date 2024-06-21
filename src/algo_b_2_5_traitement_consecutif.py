def traitement_consecutifs(pln_a, pln_b):
    # TRAITEMENT CONSÉCUTIFS
    if pln_b['callsignprevu'] == pln_a['callsignprevu']:
        traitement_1(pln_a,pln_b)
    elif pln_b['callsignprevu'][:3] == "AFR" and pln_a[:3] == "AFR":
        traitement_2(pln_a,pln_b)
    else:
        traitement_4(pln_a,pln_b)
        if pln_b['callsignprevu'] == pln_a['callsignprevu']:
            traitement_1(pln_a,pln_b)
        else:
            traitement_2(pln_a,pln_b)
    
def traitement_1(pln_a,pln_b):
    pass

def traitement_2(pln_a,pln_b):
    pass

def traitement_4(pln_a,pln_b):
    pass

# Exemple d'utilisation de la fonction
pln_a = "ExemplePLNA"
pln_b = "ExemplePLNB"
traitement_consecutifs(pln_a, pln_b)
