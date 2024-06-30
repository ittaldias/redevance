
import pytest
import pandas as pd
from src.stan import read_and_process_file, convert_and_calculate

def pytest_addoption(parser):
    parser.addoption(
        '--output',  # Assurez-vous d'utiliser le double tiret ici.
        action='store',
        default='',
        help='Chemin vers le fichier DataFrame récupéré de la lecture de stan'
    )

@pytest.fixture
def output_data(request):
    output_path = request.config.getoption('--output')
    # Charger les données seulement si le chemin n'est pas vide
    if output_path:
        return pd.read_csv(output_path)
    return None  # Ou charger une donnée par défaut ou gérer une exception selon vos besoins
@pytest.fixture(scope="session")
def output_data():
    # Load and process data file once for all tests in the session
    output = read_and_process_file("data/RDVC-20230522.pln")
    processed_output = convert_and_calculate(output)
    return processed_output
