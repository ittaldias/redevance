import pandas as pd
import numpy as np
import pytest
from datetime import datetime, timedelta
from src.stan import read_and_process_file, convert_and_calculate
#TEST GIT
output, date_obj = read_and_process_file("data/RDVC-20230522.pln")
output = convert_and_calculate(output, date_obj)
date_str = '22-05-2023'
date_obj = datetime.strptime(date_str, "%d-%m-%Y")

def test_dateRelative_realise_HeurePremiereBaliseActive_realise_jourdarchive():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'SWR9G', 'heure_de_reference'].values[0]
    assert heure_de_reference == 465.0, print(output.info())

def test_dateRelative_final_HeurePremiereBaliseActive_realise_veille():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'AFR903A', 'heure_de_reference'].values[0]
    assert heure_de_reference == 365.0, "heure_de_reference for AFR903A is not equal to 365.0"
    
def test_dateRelative_realise_HeurePremiereBaliseActive_realise_lendemain():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'EZY37KC', 'heure_de_reference'].values[0]
    assert heure_de_reference == -1440.0, "heure_de_reference for EZY37KC is not equal to -1440.0"
    
def test_dateRelative_realise_HeurePremiereBaliseActive_realise_veille():
    heure_de_reference=output.loc[output['callSign_prevu'] == 'TRA79Y', 'heure_de_reference'].values[0]
    assert heure_de_reference == 1720.0, "heure_de_reference for TRA79Y is not equal to 1720.0"
    
def test_dateRelative_realise_HeurePremiereBaliseActive_final_jourdarchive():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'SWR9G', 'heure_de_reference'].values[0]
    assert heure_de_reference == 465.0, "heure_de_reference for SWR9G is not equal to 465.0"
    
def test_dateRelative_realise_HeurePremiereBaliseActive_final_lendemain():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'EZY37KC', 'heure_de_reference'].values[0]
    assert heure_de_reference == -1440.0, "heure_de_reference for EZY37KC is not equal to -1440.0"
    
def test_dateRelative_realise_HeurePremiereBaliseActive_final_veille():
    heure_de_reference=output.loc[output['callSign_prevu'] == 'TRA79Y', 'heure_de_reference'].values[0]
    assert heure_de_reference == 1720.0, "heure_de_reference for TRA79Y is not equal to 1720.0"
    
def test_dateRelative_realise_HeurePremiereBalise_final_jourdarchive():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'SWR9G', 'heure_de_reference'].values[0]
    assert heure_de_reference == 465.0, "heure_de_reference for SWR9G is not equal to 465.0"
    
def test_dateRelative_realise_HeurePremiereBalise_final_lendemain():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'EZY37KC', 'heure_de_reference'].values[0]
    assert heure_de_reference == -1440.0, "heure_de_reference for EZY37KC is not equal to -1440.0"
    
def test_dateRelative_realise_HeurePremiereBalise_final_veille():
    heure_de_reference=output.loc[output['callSign_prevu'] == 'TRA79Y', 'heure_de_reference'].values[0]
    assert heure_de_reference == 1720.0, "heure_de_reference for TRA79Y is not equal to 1720.0"
    
def test_dateRelative_final_HeurePremiereBaliseActive_realise_jourdarchive():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'SWR9G', 'heure_de_reference'].values[0]
    assert heure_de_reference == 465.0, "heure_de_reference for SWR9G is not equal to 465.0"
    
def test_dateRelative_final_HeurePremiereBaliseActive_realise_lendemain():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'EZY37KC', 'heure_de_reference'].values[0]
    assert heure_de_reference == -1440.0, "heure_de_reference for EZY37KC is not equal to -1440.0"
    
def test_dateRelative_final_HeurePremiereBaliseActive_realise_veille():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'AFR903A', 'heure_de_reference'].values[0]
    assert heure_de_reference == 365.0, "heure_de_reference for AFR903A is not equal to 365.0"
    
def test_dateRelative_final_HeurePremiereBaliseActive_final_jourdarchive():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'AFR903A', 'heure_de_reference'].values[0]
    assert heure_de_reference == 365.0, "heure_de_reference for AFR903A is not equal to 365.0"
    
def test_dateRelative_final_HeurePremiereBaliseActive_final_lendemain():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'EZY37KC', 'heure_de_reference'].values[0]
    assert heure_de_reference == -1440.0, "heure_de_reference for EZY37KC is not equal to -1440.0"
    
def test_dateRelative_final_HeurePremiereBaliseActive_final_veille():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'EFW2865', 'heure_de_reference'].values[0]
    assert heure_de_reference == 2665.0, "heure_de_reference for EFW2865 is not equal to 2665.0"
    
def test_dateRelative_final_HeurePremiereBalise_final_jourdarchive():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'AFR903A', 'heure_de_reference'].values[0]
    assert heure_de_reference == 365.0, "heure_de_reference for AFR903A is not equal to 365.0"
    
def test_dateRelative_final_HeurePremiereBalise_final_lendemain():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'EZY37KC', 'heure_de_reference'].values[0]
    assert heure_de_reference == -1440.0, "heure_de_reference for EZY37KC is not equal to -1440.0"
    
def test_dateRelative_final_HeurePremiereBalise_final_veille():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'EFW2865', 'heure_de_reference'].values[0]
    assert heure_de_reference == 2665.0, "heure_de_reference for EFW2865 is not equal to 2665.0"
    
def test_dateRelative_realise_jourdarchive():
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    dt = date_obj + timedelta(days=1)
    dt64 = output.loc[output['callSign_prevu'] == 'EFW2865', 'date_de_reference'].values[0]
    
    # Convert dt64 to datetime
    if pd.notna(dt64):
     dt64_as_dt = pd.to_datetime(dt64)
    # Now dt64_as_dt should be a valid datetime object
    else:
    # Handle the case where dt64 is None or NaN
     dt64_as_dt = date_obj
    
    # Convert dt to datetime64
    
    # Assert statements
    assert dt == dt64_as_dt, f"Expected {dt} to equal {dt64_as_dt}"
def test_dateRelative_realise_lendemain():
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    dt = date_obj
    dt64 = output.loc[output['callSign_prevu'] == '160B', 'date_de_reference'].values[0]
    
    # Convert dt64 to datetime
    if pd.notna(dt64):
     dt64_as_dt = pd.to_datetime(dt64)
    # Now dt64_as_dt should be a valid datetime object
    else:
    # Handle the case where dt64 is None or NaN
     dt64_as_dt = date_obj
    
    # Convert dt to datetime64
    assert dt == dt64_as_dt, f"Expected {dt} to equal {dt64_as_dt}"
def test_dateRelative_realise_veille():
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    dt = date_obj + timedelta(days=1)
    dt64 = output.loc[output['callSign_prevu'] == 'EFW2865', 'date_de_reference'].values[0]
    
    # Convert dt64 to datetime
    if pd.notna(dt64):
     dt64_as_dt = pd.to_datetime(dt64)
    # Now dt64_as_dt should be a valid datetime object
    else:
    # Handle the case where dt64 is None or NaN
     dt64_as_dt = date_obj
    
    assert dt == dt64_as_dt, f"Expected {dt} to equal {dt64_as_dt}"
def test_dateRelative_final_jourdarchive():
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    dt = date_obj - timedelta(days=1)
    dt64 = output.loc[output['callSign_prevu'] == 'EZY37KC', 'date_de_reference'].values[0]
    
    # Convert dt64 to datetime
    if pd.notna(dt64):
     dt64_as_dt = pd.to_datetime(dt64)
    # Now dt64_as_dt should be a valid datetime object
    else:
    # Handle the case where dt64 is None or NaN
     dt64_as_dt = date_obj
    
    assert dt == dt64_as_dt, f"Expected {dt} to equal {dt64_as_dt}"
def test_dateRelative_final_lendemain():
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    dt = date_obj
    dt64 = output.loc[output['callSign_prevu'] == 'AFR903A', 'date_de_reference'].values[0]
    
    # Convert dt64 to datetime
    if pd.notna(dt64):
     dt64_as_dt = pd.to_datetime(dt64)
    # Now dt64_as_dt should be a valid datetime object
    else:
    # Handle the case where dt64 is None or NaN
     dt64_as_dt = date_obj
    
    assert dt == dt64_as_dt, f"Expected {dt} to equal {dt64_as_dt}"
def test_dateRelative_final_veille():
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    dt = date_obj
    dt64 = output.loc[output['callSign_prevu'] == 'SWR9G', 'date_de_reference'].values[0]
    
    # Convert dt64 to datetime
    if pd.notna(dt64):
     dt64_as_dt = pd.to_datetime(dt64)
    # Now dt64_as_dt should be a valid datetime object
    else:
    # Handle the case where dt64 is None or NaN
     dt64_as_dt = date_obj
    
    assert dt == dt64_as_dt, f"Expected {dt} to equal {dt64_as_dt}"
    
    
def test_set_typePln_RPL():
    pln = output.loc[output['callSign_prevu'] == 'TRA79Y', 'typePlnStan'].values[0]
    assert pln == 'FPL', "Expected 'RPL', but got the wrong one"

def test_set_typePln_APL():
    pln = output.loc[output['callSign_prevu'] == 'TRA79Y', 'typePlnStan'].values[0]
    assert pln == 'FPL', "Expected 'RPL', but got the wrong one"
def test_set_typePln_ABI():
    pln = output.loc[output['callSign_prevu'] == 'TRA79Y', 'typePlnStan'].values[0]
    assert pln == 'FPL', "Expected 'RPL', but got the wrong one"
