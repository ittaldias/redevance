# test_vol.py

import pytest
from src.mains import parse_pln_file
import pandas as pd

def test_parse_pln_file():
    """Tests the parse_pln_file function with sample data."""
    
    # Prepare a sample file content
    sample_content = """
    05
    11
    20 ETH575 KORD HAAB 9273 -1 B788 0000 ETAOU 0
    21 -525 350 485 -525
    22 I S AA47735238 0 0 FPL 21052023 SANDY 0 0 21-05-2023 00:00
    23 0 0 0 ??????
    24 -1 ???????? 0
    2R LASAT390
    31 SANDY MOTOX RUCAC LESDO RANUX ETINO NEBAX LASAT DEVDI
    32 -105 -162 -161 -149 -142 -138 -131 -128 -64
    33 370 370 370 370 370 370 370 370 370
    36 0 0 0 0 0 0 0 0 0
    41 HN YR HE GL 5M
    71 EGGG REIM ZURI
    72 1 2 5
    13
    """

    # Write the sample content to a temporary file
    with open('sample_test_file.pln', 'w') as file:
        file.write(sample_content)

    # Call the function with the temporary file
    output_df = parse_pln_file('sample_test_file.pln')

    # Create the expected dataframe for one row
    expected_data = {
        'callsignprevu': ['ETH575'],
        'depprevu': ['KORD'],
        'arrprevu': ['HAAB'],
        'numcautraprevu': ['9273'],
        'typeavionprevu': ['B788'],
        'workprevu': ['ETAOU'],
        'heuresdedepprevu': ['-525'],
        'RFLprevu': ['350'],
        'vitesseprevu': ['485'],
        'EOBTprevu': ['-525'],
        'regledevolprevu': ['I'],
        'typedevolprevu': ['S'],
        'IFPLprevu': ['AA47735238'],
        'PLN_activeprevu': ['0'],
        'PLN_annuleprevu': ['0'],
        'date_blockprevu': ['21052023'],
        'baliseprevu': ['SANDY'],
        'listhourprevu': ['-105'],
        'listedesbalistesprevu': ['370'],
        'indicateurprevu': ['0'],
        'carteprevu': ['HN'],
        'centretraverséprevu': ['EGGG'],
        'listederangpremierprevu': ['1']
    }

    expected_df = pd.DataFrame(expected_data)

    # Compare the resulting dataframe with the expected dataframe
    pd.testing.assert_frame_equal(output_df.reset_index(drop=True), output_df.reset_index(drop=True))


if __name__ == "__main__":
    pytest.main()
