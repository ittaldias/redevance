# conftest.py

import pytest
import pandas as pd

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
