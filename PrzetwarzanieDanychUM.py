import pandas as pd

excel_path = 'data.xlsx'
df = pd.read_excel(excel_path)
# Usuwanie pustej kolumny
df = df.drop(columns=['Column1'])
# Przekształcenie wawrtości diagnozy na wlasnosci liczbowe
df['diagnosis'] = df['diagnosis'].replace({'M': 1, 'B': 0})
# Wybieranie optymalnych kolumn z bazy danych
dane_do_modelu = [
    'diagnosis',
    'texture_mean',
    'area_mean',
    'concavity_mean',
    'symmetry_mean',
    'fractal_dimension_mean',
    'area_se',
    'concavity_se',
    'smoothness_worst',
    'fractal_dimension_worst'
]
df = df[dane_do_modelu]
df = df.drop_duplicates()
df = df.dropna()
# Zapisanie pliku
df.to_excel('przetworzone-dane.xlsx', index=False)
