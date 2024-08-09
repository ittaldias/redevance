import pandas as pd
import numpy as np
import re

# Fonction pour convertir un modèle en expression régulière
def get_valid_value(element, columns):
        for col in columns:
            if col in element and not(element[[col]].isna().iloc[0]):
                return element[col]
        return ""

def format_flight_message(row):
    sequence_number = f"{row.name + 1:04}"
    intro_correction_code = "F"
    valeur = int(get_valid_value(row, ['heure_de_reference']))
    heure = (valeur%1440)//60
    min = (valeur%1440)%60
    time_of_departure = f"{(100*heure + min):04}"
    aerodrome_of_departure = get_valid_value(row, ['dep_realise', 'dep_final', 'de_prevu']).ljust(4)
    aerodrome_of_arrival = get_valid_value(row, ['arr_realise', 'arr_final', 'arr_prevu']).ljust(4)
    flight_identification = get_valid_value(row, ['callSign_realise', 'callSign_final', 'callSign_prevu']).ljust(9)
    main_exemption_code = row["code_d_exoneration"].ljust(1)
    aircraft_type = get_valid_value(row, ['typeAvion_realise', 'typeAvion_final', 'typeAvion_prevu']).ljust(7)
    operator = str(row["code_exploitant"]).ljust(3)
    aircraft_registration = str(get_valid_value(row, ['work1realise', 'work1final', 'work1prevu'])).ljust(9)
    comment = ""
    est_off_block_date = get_valid_value(row, ['date_de_reference']).ljust(6)
    ifplid = get_valid_value(row, ['IFPL_realise', 'IFPL_final', 'IFPL_prevu']).ljust(9)
    initial_aerodrome_destination = ""
    charging_zone_overflown = ""
    entry_point_coordinates = ""
    exit_point_coordinates = ""
    supplementary_exemption_codes = ""
    source_icao_address = ""
    icao_address = get_valid_value(row, ['adresseModeS_realise', 'adresseModeS_final', 'adresseModeS_prevu']).ljust(6)
    additional_comment = ""
    front_alg_fr = row["front_alg_fr"]
    premier_plot_fr = str(row["premier_plot_fr"])
    modes_fr = str(row["modes_fr"])

    return {
        "Sequence number": sequence_number,
        "Code": intro_correction_code,
        "Time of departure/entry": time_of_departure,
        "Departure aerodrome": aerodrome_of_departure,
        "Arrival aerodrome": aerodrome_of_arrival,
        "Flight identification": flight_identification,
        "Main Exemption code": main_exemption_code,
        "Type of aircraft": aircraft_type,
        "Operator": operator,
        "Aircraft Registration": aircraft_registration,
        "Comment1": comment,
        "Flight date": est_off_block_date,
        "IFPLID": ifplid,
        "Planned_aerodrome": initial_aerodrome_destination,
        "Charging_zone_overflow": charging_zone_overflown,
        "Entry_point": entry_point_coordinates,
        "Exit_point": exit_point_coordinates,
        "Sup_exemption_code": supplementary_exemption_codes,
        "Source of the Aircraft Address": source_icao_address,
        "24-bit Aircraft Address": icao_address,
        "Comment2": additional_comment,
        "case7" : str(row["case7"]),
        "case8" : str(row["case8"]),
        "case9" : str(row["case9"]),
        "case10" : str(row["case10"]),
        "case13" : str(row["case13"]),
        "case15" : str(row["case15"]),
        "case16" : str(row["case16"]),
        "case18" : str(row["case18"]),
        "ccrArrival" : str(row["ccrArrival"]),
        "front_alg_fr" : front_alg_fr,
        "premier_plot_fr" : premier_plot_fr,
        "modes_fr" : modes_fr
    }
