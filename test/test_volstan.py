# test_volstan.py

import pytest
from src.mains import parse_pln_file
import pandas as pd

def test_parse_pln_file():
    """Tests the parse_pln_file function with sample data."""
    
    # Prepare a sample file content
    sample_content = """
    05
    11
    20 RYR850Z GMMX EBCI 1659 0 B738 0000 EIENX 0
    21 345 360 443 345
    22 I S AA47747089 0 0 FPL 22052023 MADR1 0 0 22-05-2023 00:00
    23 0 1 0 ??????
    24   -1 ???????? 0
    2R ADABI360
    31 MADR1 LUSEM BZ2WM LULUT BZ1BR BR1BZ ADABI BR1AX BOKNO DEVRO VANAD PIWIZ VADOM BAMES PODEM SOMIL BELDI VEKIN ARVOL NIVOR 
    32 466 467 469 477 478 479 496 498 500 503 506 509 512 515 518 523 525 530 532 538 
    33 380 380 380 380 380 380 380 380 360 360 340 340 340 340 340 309 310 197 160 160 
    36 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    41 PP Z4 R4 R3 XI XS ZS TB UN WL 
    71 MADR BORD BRST REIM PARI EBBR 
    72 1 2 5 8 9 10 
    13
    20 RYR850Z GMMX EBCI 1659 0 B738 1000 EIENX 0
    21 345 360 443 345
    22 I S AA47747089 1 0 FPL 22052023 MADR1 0 0 22-05-2023 00:00
    23 0 1 0 4CA8E9
    24   -1 ???????? 0
    """

    # Write the sample content to a temporary file
    with open('sample_test_file.pln', 'w') as file:
        file.write(sample_content)

    # Call the function with the temporary file
    output_df = parse_pln_file('sample_test_file.pln')

    # Create the expected dataframe for one row
    expected_data = {
        'callsignprevu': ['RYR850Z'],
        'depprevu': ['GMMX'],
        'arrprevu': ['EBCI'],
        'numcautraprevu': ['1659'],
        'typeavionprevu': ['B738'],
        'workprevu': ['EIENX'],
        'heuresdedepprevu': ['345'],
        'RFLprevu': ['360'],
        'vitesseprevu': ['443'],
        'EOBTprevu': ['345'],
        'regledevolprevu': ['I'],
        'typedevolprevu': ['S'],
        'IFPLprevu': ['AA47747089'],
        'PLN_activeprevu': ['0'],
        'PLN_annuleprevu': ['0'],
        'date_blockprevu': ['22052023'],
        'baliseprevu': ['MADR1'],
        'listhourprevu': ['466'],
        'listedesbalistesprevu': ['380'],
        'indicateurprevu': ['0'],
        'carteprevu': ['PP'],
        'centretraverséprevu': ['MADR'],
        'listederangpremierprevu': ['1']
    }

    expected_df = pd.DataFrame(expected_data)

    # Compare the resulting dataframe with the expected dataframe
    pd.testing.assert_frame_equal(output_df.reset_index(drop=True), output_df.reset_index(drop=True))

if __name__ == "__main__":
    pytest.main()
