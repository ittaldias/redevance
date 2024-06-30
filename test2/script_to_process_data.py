import pandas as pd
import numpy as np
import pytest
from datetime import datetime, timedelta
from src.stan import read_and_process_file, convert_and_calculate

output = read_and_process_file("data/RDVC-20230522.pln")
processed_output = convert_and_calculate(output)
processed_output.to_pickle('processed_data.pkl')  # Save processed data to a file
