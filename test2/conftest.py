# test2/conftest.py
import pytest
import pandas as pd
from src.stan import read_and_process_file, convert_and_calculate
from src.algo_b_2_3_traitement_preliminaire import traitement_utile_inutile
from src.algo_b_2_4_bis_traitement_unitaire import traitement_unitaire

def pytest_addoption(parser):
    parser.addoption(
        "--output",
        action="store",
        default="data/RDVC-20230522.pln",
        help="Path to the data file to be processed"
    )
@pytest.fixture
def output_data(request):
    file_path = request.config.getoption("--output")
    output_data = read_and_process_file("data/RDVC-20230522.pln",)
    output_data = traitement_utile_inutile(output_data)
    output_data = convert_and_calculate(output_data)
    output_data = traitement_unitaire(output_data)
    return output_data

