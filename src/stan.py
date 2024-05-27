from datetime import datetime
import pandas as pd
import numpy as np

def parse_pln_file(file_path):
    vol_prevu = []
    vol_fini = []
    vol_termine = []
    tableau_vol = {}
    tableaux_vol = []
    iter = 0
    flag82 = False
    hneg = False
    compt82 = 0
    num81 = 0
    prevu = False
    termine = False
    final = False
    complet = 0
    output = pd.DataFrame()
    compteur = 0

    with open(file_path, 'r') as fichier:
        for i, ligne in enumerate(fichier):
            words = ligne.strip().split()
            if not words:
                continue

            if words[0] == "02":
                # Extract date
                date_str = words[1]
                try:
                    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
                except ValueError:
                    print(f"Error parsing date: {ligne}")
                    continue
                date_fichier = date_obj.timetuple().tm_yday
            if words[0] == "05":
                if tableau_vol:
                    df_dictionary = pd.DataFrame([tableau_vol])
                    output = pd.concat([output, df_dictionary], ignore_index=True)

                tableau_vol = {}
                balise = ''
                hneg = False
                flag82 = False
                etat = ''
            if words[0] in ["11", "12", "13", "14"]:
                etat = {'11': 'prevu', '12': 'final', '13': 'realise', '14': 'transaction'}[words[0]]
            if words[0] == "20":
                tableau_vol.update({
                    f'callsign{etat}': words[1],
                    f'dep{etat}': words[2],
                    f'arr{etat}': words[3],
                    f'numcautra{etat}': words[4],
                    f'typeavion{etat}': words[6],
                    f'work{etat}': words[7]
                })
                if words[8][:2] != '??':
                    pass
            if words[0] == "21":
                tableau_vol.update({
                    f'heuresdedep{etat}': words[1],
                    f'RFL{etat}': words[2],
                    f'vitesse{etat}': words[3],
                    f'EOBT{etat}': words[4]
                })
            if words[0] == "22":
                tableau_vol.update({
                    f'regledevol{etat}': words[1],
                    f'typedevol{etat}': words[2],
                    f'PLN_active{etat}': words[4],
                    f'PLN_annule{etat}': words[5]
                })
                if words[3][:2] != '??':
                    tableau_vol[f'IFPL{etat}'] = words[3].strip().ljust(10)
                if '??' not in words[7] and len(words[7]) == 8:
                    date_str = words[7]
                    date_obj = datetime.strptime(date_str, '%d%m%Y')
                    day_vol = date_obj.timetuple().tm_yday
                    tableau_vol[f'date_block{etat}'] = words[7][:4] + words[7][6:]
                else:
                    tableau_vol[f'date_block{etat}'] = words[7].strip().ljust(6)
            if words[0] == "23":
                tableau_vol[f'adressemode{etat}'] = np.NaN if "??" in words[4] else words[4]
            if words[0] == "24":
                tableau_vol.update({
                    f'numeroPLNM{etat}': words[1],
                    f'FlightID{etat}': words[2]
                })
            if words[0] == "31":
                tableau_vol[f'balise{etat}'] = words[1]
            if words[0] == "32":
                tableau_vol[f'listhour{etat}'] = words[1]
            if words[0] == "33":
                tableau_vol[f'listedesbalistes{etat}'] = words[1]
            if words[0] == "36":
                tableau_vol[f'indicateur{etat}'] = words[1]
            if words[0] == "41":
                tableau_vol[f'carte{etat}'] = words[1]
            if words[0] == "71":
                tableau_vol[f'centretraversé{etat}'] = words[1]
            if words[0] == "72":
                tableau_vol[f'listederangpremier{etat}'] = words[1]
            if words[0] == "80":
                tableau_vol[f'rangtransaction{etat}'] = words[1]
            if words[0] == "81":
                if len(words) >= 15:
                    parts = ligne.split("-")
                    last_word = parts[0].split()[-1]
                    if "(FPL" in parts[0] or "(CHG)" in parts[0]:
                        tableau_vol.update({
                            'case7': parts[1],
                            'case8': parts[2],
                            'case9': parts[3],
                            'case10': parts[4],
                            'case13': parts[5],
                            'case15': parts[6],
                        })
                        if len(parts) > 8:
                            tableau_vol['case16'] = parts[7]
                            tableau_vol['case18'] = parts[8]
                        else:
                            print(ligne)
                            compteur += 1
                    elif "(APL" in parts[0]:
                        tableau_vol.update({
                            'case7': parts[1],
                            'case8': parts[2],
                            'case9': parts[3],
                            'case10': parts[4],
                            'case13': parts[5],
                            'case15': parts[6],
                        })
                        if len(parts) > 8:
                            tableau_vol['case16'] = parts[7]
                            tableau_vol['case18'] = parts[-1]
                        else:
                            print(ligne)
                            compteur += 1
            if words[0] == "82":
                tableau_vol.update({
                    'heure': words[1][:2],
                    'minute': words[1][3:],
                    f'accusetrt{etat}': words[1]
                })
                if "CCR:" in ligne:
                    compteur_CCr = 0
                    for word in words:
                        compteur_CCr += 1
                        if word == "CCR:":
                            break
                    tableau_vol['ccr_arrival'] = words[compteur_CCr]
            if words[0] == "84":
                tableau_vol[f'final{etat}'] = words[1]

    return output
