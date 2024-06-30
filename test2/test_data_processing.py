# test_data_processing.py

def test_data_integrity(output_data):
    assert not output_data.empty, "Le DataFrame ne doit pas être vide"
    assert 'some_important_column' in output_data.columns, "Colonne essentielle manquante"

def test_specific_data_feature(output_data):
    # Supposons que vous voulez vérifier une caractéristique spécifique des données
    assert output_data['some_important_column'].mean() > 10, "La moyenne doit être supérieure à 10"
