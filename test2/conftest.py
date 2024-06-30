# conftest.py
import pytest
import pandas as pd
from src.stan import read_and_process_file, convert_and_calculate

@pytest.fixture(scope="session")
def output_data():
    # Load and process data file once for all tests in the session
    output = read_and_process_file("data/RDVC-20230522.pln")
    processed_output = convert_and_calculate(output)
    return processed_output
