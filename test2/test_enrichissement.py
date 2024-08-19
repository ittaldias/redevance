from datetime import datetime, timedelta
import pandas as pd

# Initial setup
output, date_obj = read_and_process_file("data/RDVC-20230522.pln")
output = convert_and_calculate(output, date_obj)
date_str = '22-05-2023'
date_obj = datetime.strptime(date_str, "%d-%m-%Y")

# Dynamic analysis function
def dynamic_analysis(target_date_str):
    target_date = datetime.strptime(target_date_str, "%d-%m-%Y")

    # Calculate the previous and next days
    previous_day = target_date - timedelta(days=1)
    next_day = target_date + timedelta(days=1)

    # Format the dates to match the file naming convention
    previous_day_str = previous_day.strftime("%Y%m%d")
    target_date_str = target_date.strftime("%Y%m%d")
    next_day_str = next_day.strftime("%Y%m%d")

    # Construct file paths
    nom_fichier_jour_1 = f'/content/drive/MyDrive/data/stan_mars_2024/RDVC-{previous_day_str}.pln'
    nom_fichier_jour_2 = f'/content/drive/MyDrive/data/stan_mars_2024/RDVC-{target_date_str}.pln'
    nom_fichier_jour_3 = f'/content/drive/MyDrive/data/stan_mars_2024/RDVC-{next_day_str}.pln'

    # Read and process files
    fichier_jour_1 = read_and_process_file(nom_fichier_jour_1)
    fichier_jour_2 = read_and_process_file(nom_fichier_jour_2)
    fichier_jour_3 = read_and_process_file(nom_fichier_jour_3)

    # Convert and calculate
    jour_1 = convert_and_calculate(fichier_jour_1, previous_day)
    jour_2 = convert_and_calculate(fichier_jour_2, target_date)
    jour_3 = convert_and_calculate(fichier_jour_3, next_day)

    return jour_1, jour_2, jour_3

# Additional processing functions
def traitement_utile_inutile(df):
    df['utile_inutile'] = df.apply(utile_inutile, axis=1)
    return df

def ajouter_colonne_doublon(df, tolerance_minutes=19):
    df['doublon'] = False
    df = df.sort_values(by=['callSign_prevu', 'heure_de_reference']).reset_index(drop=True)
    i = 1
    while i < len(df):
        if df.at[i, 'callSign_prevu'] == df.at[i - 1, 'callSign_prevu']:
            delta = abs((df.at[i, 'heure_de_reference'] - df.at[i - 1, 'heure_de_reference']))
            if delta <= tolerance_minutes:
                df = df.drop(i).reset_index(drop=True)
                continue  # Reevaluate the same index after dropping
        i += 1
    return df

def supprimer_doublons(df):
    return df[df['doublon'] == False].drop(columns=['doublon'])

def format_flight_message(row):
    sequence_number = f"{row.name + 1:04}"
    intro_correction_code = "F"
    valeur = int(get_valid_value(row, ['heure_de_reference']))
    heure = (valeur % 1440) // 60
    min = (valeur % 1440) % 60
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
        "case7": str(row["case7"]),
        "case8": str(row["case8"]),
        "case9": str(row["case9"]),
        "case10": str(row["case10"]),
        "case13": str(row["case13"]),
        "case15": str(row["case15"]),
        "case16": str(row["case16"]),
        "case18": str(row["case18"]),
        "ccrArrival": str(row["ccrArrival"]),
        "front_alg_fr": front_alg_fr,
        "premier_plot_fr": premier_plot_fr,
        "modes_fr": modes_fr
    }

# Execute the dynamic analysis
dateAnalyse = '21-03-2024'
jour_1, jour_2, jour_3 = dynamic_analysis(dateAnalyse)

# Process the data
jour_1_utile_inutile = traitement_utile_inutile(jour_1)
jour_2_utile_inutile = traitement_utile_inutile(jour_2)
jour_3_utile_inutile = traitement_utile_inutile(jour_3)

jour_1_utile = jour_1_utile_inutile[jour_1_utile_inutile["utile_inutile"] == "UTI"].copy()
jour_2_utile = jour_2_utile_inutile[jour_2_utile_inutile["utile_inutile"] == "UTI"].copy()
jour_3_utile = jour_3_utile_inutile[jour_3_utile_inutile["utile_inutile"] == "UTI"].copy()

jour_1_utile_traitee = traitement_unitaire(jour_1_utile)
jour_2_utile_traitee = traitement_unitaire(jour_2_utile)
jour_3_utile_traitee = traitement_unitaire(jour_3_utile)

# Handle duplicates
jour_1_utile_traitee_avec_doublons_false = ajouter_colonne_doublon(jour_1_utile_traitee)
jour_2_utile_traitee_avec_doublons_false = ajouter_colonne_doublon(jour_2_utile_traitee)
jour_3_utile_traitee_avec_doublons_false = ajouter_colonne_doublon(jour_3_utile_traitee)

jour_1_utile_traitee_sans_doublons = supprimer_doublons(jour_1_utile_traitee_avec_doublons_false)
jour_2_utile_traitee_sans_doublons = supprimer_doublons(jour_2_utile_traitee_avec_doublons_false)
jour_3_utile_traitee_sans_doublons = supprimer_doublons(jour_3_utile_traitee_avec_doublons_false)

# Combine and further process the data
jour_123 = pd.concat([jour_1_utile_traitee_sans_doublons, jour_2_utile_traitee_sans_doublons, jour_3_utile_traitee_sans_doublons], ignore_index=True)
jour_123['date_de_reference'] = jour_123['date_de_reference'].dt.strftime('%y%m%d')
jour_123 = jour_123[jour_123["vol_a_transmettre"] == True]

# Continue with additional processing as required
