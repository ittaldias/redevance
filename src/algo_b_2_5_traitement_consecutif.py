from datetime import datetime
import re

# Traiter les cas où les PLN sont de type "RPL" et vérifier la différence de temps
def traitement_1(pln_a, pln_b):
    # Calculer la différence de temps en minutes
    time_diff = abs((pln_b['heure_de_reference'] - pln_a['heure_de_reference']).total_seconds() / 60)

    # Appliquer les règles spécifiques si les conditions sont remplies
    if pln_a['typePlnRDVC'] == "RPL" and pln_b['typePlnRDVC'] == "RPL" and time_diff > 720:
        if pln_a['vol_a_transmettre'] == 'FAUX' and pln_b['vol_a_transmettre'] == 'FAUX':
            if pln_a['typeAvion_prevu'] != pln_b['typeAvion_prevu'] and pln_a['typeAvion_prevu'] != "ZZZZ" and pln_b['typeAvion_prevu'] != "ZZZZ":
                pln_a['PLN_valide'] = False
                pln_b['PLN_valide'] = False
                return "Erreur type d'avion ('TYPVAV1')"
            elif pln_a['dep_prevu'] == pln_b['dep_prevu'] and pln_a['arr_prevu'] == pln_b['arr_prevu']:
                if pln_a['exoneration_code'] != pln_b['exoneration_code'] and pln_b['typePlnRDVC'] == "RPL" and "French" in pln_a['company']:
                    pln_a['PLN_valide'] = False
                    pln_b['PLN_valide'] = False
                    return "Erreur exoneration ('EXON')"
                else:
                    return "Conditions pour un traitement double supplémentaire rencontrées"
            else:
                return "Les PLN ont des lieux de départ ou d'arrivée distincts"
        else:
            return "Au moins un PLN doit être transmis"
    else:
        return "Les critères de type RPL ou de différence de temps ne sont pas remplis"

# Traiter les vols coordonnés en vérifiant les indicatifs et les compagnies
def traitement_2(pln_a, pln_b, compagnies_coordonnees):
    # Calculer la différence de temps en minutes
    time_diff = abs((pln_b['heure_de_reference'] - pln_a['heure_de_reference']).total_seconds() / 60)

    # Appliquer des règles de coordination basées sur les indicatifs et les compagnies
    if (pln_a['vol_a_transmettre'] == 'FAUX' or pln_b['vol_a_transmettre'] == 'FAUX') and time_diff > 720:
        if pln_a['indicatif'][:3] == pln_b['indicatif'][:3] and pln_a['indicatif'][-1].isdigit() and pln_b['indicatif'][-1].isdigit():
            num_a = int(''.join(filter(str.isdigit, pln_a['indicatif'][-3:])))
            num_b = int(''.join(filter(str.isdigit, pln_b['indicatif'][-3:])))
            if num_b == num_a + 1 and pln_a['indicatif'][:-3] == pln_b['indicatif'][:-3]:
                if any(pln_a['indicatif'][3] in interval for interval in compagnies_coordonnees):
                    if pln_a['indicatif'][-1] in '02468':
                        if pln_a['indicatif'] in compagnies_coordonnees and compagnies_coordonnees[pln_a['indicatif']] % 2 == 0:
                            return "Procéder au traitement du vol coordonné"
                    return "Fin du traitement : Condition de parité non remplie"
                return "Fin du traitement : Aucun intervalle valide trouvé"
            return "Fin du traitement : Les parties numériques ou les caractères ne correspondent pas"
    return "Conditions initiales non remplies"
from datetime import datetime
import re

# Vérifier et gérer les indicatifs des compagnies françaises
def traitement_4(pln_a, pln_b, compagnies_francaises):
    """
    Vérifie si l'indicatif du PLN B correspond aux critères des compagnies françaises.
    Modifie les indicatifs de PLN A et B pour comparaison s'ils répondent aux conditions spécifiées.
    """
    if pln_b['indicatif'][:2] in compagnies_francaises and pln_b['indicatif'].endswith('N'):
        # Modifier l'indicatif de PLN A s'il répond au format spécifié
        if len(pln_a['indicatif']) > 4 and pln_a['indicatif'][-2].isdigit() and pln_a['indicatif'][-1].isalpha():
            pln_a['indicatif_pour_comparaison'] = pln_a['indicatif'][:-2]
        # Modifier l'indicatif de PLN B s'il répond au format spécifié
        if len(pln_b['indicatif']) > 4 and pln_b['indicatif'][-2].isdigit() and pln_b['indicatif'][-1].isalpha():
            pln_b['indicatif_pour_comparaison'] = pln_b['indicatif'][:-2]
        
        return "Indicatifs modifiés pour comparaison."
    else:
        return "Aucune modification nécessaire."

# Exemple d'utilisation
compagnies_francaises = {'AF', 'SS'}  # Ensemble d'exemple de bigrammes de compagnies françaises
pln_a = {'indicatif': 'AF1234K'}
pln_b = {'indicatif': 'AF5678N'}
resultat = traitement_4(pln_a, pln_b, compagnies_francaises)
print(resultat)


# Traiter les vols consécutifs selon les indicatifs
def traitement_consecutifs(pln_a, pln_b):
    """
    Applique les traitements appropriés si les PLN ont des indicatifs prévus consécutifs ou appartiennent à la même compagnie 'AFR'.
    """
    if pln_b['indicatif_prevu'] == pln_a['indicatif_prevu']:
        return traitement_1(pln_a, pln_b)
    elif pln_b['indicatif_prevu'][:3] == "AFR" and pln_a['indicatif_prevu'][:3] == "AFR":
        return traitement_2(pln_a, pln_b)
    else:
        traitement_4(pln_a, pln_b)  # Supposé que traitement_4 est applicable ici également
        if pln_b['indicatif_prevu'] == pln_a['indicatif_prevu']:
            return traitement_1(pln_a, pln_b)
        else:
            return traitement_2(pln_a, pln_b)

# Utilisation exemple
pln_a = {'indicatif_prevu': 'AFR123', 'dep_prevu': 'CDG', 'arr_prevu': 'JFK', 'PLN_valide': True, 'pln_actif': True, 'vol_a_transmettre': 'VRAI', 'action': 'A'}
pln_b = {'indicatif_prevu': 'AFR124', 'dep_prevu': 'CDG', 'arr_prevu': 'LAX', 'PLN_valide': True, 'pln_actif': False, 'vol_a_transmettre': 'VRAI', 'action': 'B'}
resultat_consecutifs = traitement_consecutifs(pln_a, pln_b)
print(resultat_consecutifs)

# Définir d'autres traitements basés sur les diagrammes visuels et les descriptions fournies
# Les fonctions traitement_1, traitement_2, etc., doivent être définies de manière similaire à traitement_4, adaptées aux spécifications détaillées du processus de gestion des vols.


# Traiter spécifiquement les PLN lors du contrôle final
def traitement_5(pln_a, pln_b, final_control):
    if final_control:
        pln_a['PLN_valide'] = False
        pln_b['PLN_valide'] = False
        pln_a['Erreur'] = 'DB0'
        pln_b['Erreur'] = 'DB0'
        pln_a['PLN_a_verifier_TC'] = True  # Flag de vérification finale
        pln_b['PLN_a_verifier_TC'] = True
        return "Actions de contrôle final exécutées : PLNs invalidés et erreurs enregistrées."
    else:
        pln_a['Annulation'] = True
        pln_b['Annulation'] = True
        return "Annulation automatique exécutée."

# Appliquer le même traitement que traitement_5 pour une uniformité dans les noms
def traitement_6(pln_a, pln_b, final_control):
    return traitement_5(pln_a, pln_b, final_control)

# Recalculer la validité du PLN basée sur des critères spécifiques
def traitement_7(pln):
    if (pln.get('Erreur') == 'NA') or \
       (not pln['plnActive_prevu'] and pln['vol_a_transmettre'] == 'VRAI' and pln['action'] in ['A', 'Q', 'V', 'W', 'C']):
        pln['PLN_valide'] = False
    else:
        pln['PLN_valide'] = True
    return f"Statut de validité du PLN recalculé : {pln['PLN_valide']}"

# Traiter les erreurs de séquence pour les PLNs avec des conditions de départ et d'arrivée spécifiques
def traitement_11(pln_a, pln_b):
    if pln_b['dep_prevu'] == pln_a['dep_prevu']:
        if pln_a['arr_prevu'] == 'France':
            pln_b['PLN_valide'] = False
            pln_a['PLN_valide'] = False
            return "Erreur de séquence 'SEQ01E'"
        else:
            if pln_b['arr_prevu'] == pln_a['arr_prevu']:
                if (pln_a['plnActive_prevu'] or pln_a['action'] in ['A', 'O']) and (pln_b['sequence_error'] == "SEQ01F"):
                    return traitement_specifique(pln_a, pln_b)
                elif (pln_b['plnActive_prevu'] or pln_b['action'] in ['A', 'O']) and (pln_a['sequence_error'] == "SEQ01F"):
                    return traitement_specifique(pln_a, pln_b)
                if pln_a['if dep_prevu'] == pln_a['arr_prevu']:
                    pln_b['PLN_valide'] = False
                    pln_a['PLN_valide'] = False
                    return "Erreur de séquence 'SEQ01F'"
            else:
                return "Aucune action nécessaire"
    else:
        if pln_b['arr_prevu'] == pln_a['arr_prevu']:
            return traitement_specifique(pln_a, pln_b)
        else:
            return "Aucune action nécessaire"

# Logique spécifique de traitement, à définir selon les besoins
def traitement_specifique(pln_a, pln_b):
    # Placeholder pour une logique de traitement spécifique basée sur les erreurs de séquence
    return "Logique de traitement spécifique ici"
