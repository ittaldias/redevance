# test2/conftest.py
import pytest
import pandas as pd
from src.stan import read_and_process_file, convert_and_calculate

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
    data = read_and_process_file("data/RDVC-20230522.pln",)
    processed_data = convert_and_calculate(data)
    return processed_data

