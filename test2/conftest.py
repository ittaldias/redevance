import pytest
import pandas as pd
from src.stan import read_and_process_file, convert_and_calculate

def pytest_addoption(parser):
    parser.addoption(
        '--output',  # Use double dashes as correctly noted.
        action='store',
        default='data/RDVC-20230522.pln',  # Default path as an example
        help='Path to the data file to be processed'
    )

@pytest.fixture(scope="session")
def output_data(request):
    output_path = request.config.getoption('--output')
    if output_path:
        try:
            raw_data = read_and_process_file(output_path)
            processed_data = convert_and_calculate(raw_data)
            return processed_data
        except Exception as e:
            pytest.fail(f"Failed to process data from {output_path}: {str(e)}", pytrace=False)
    else:
        pytest.fail("No data file path provided", pytrace=False)
