import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

excel_path = 'data.xlsx'
df = pd.read_excel(excel_path)

# 1. Normalizacja nazw kolumn (usuwa przypadkowe spacje na początku/końcu)
df.columns = df.columns.str.strip()

# 2. Pewna konwersja diagnosis na liczby 0 i 1
for col in df.columns:
    if col.lower() == 'diagnosis':
        # Zamiana wartości i konwersja na typ liczbowy float/int
        df[col] = df[col].astype(str).str.strip().map({'M': 1, 'B': 0})
        df[col] = pd.to_numeric(df[col], errors='coerce')
        df.rename(columns={col: 'diagnosis'}, inplace=True)
        break

# 3. Usunięcie kolumn 'id', 'column1' oraz pustych 'unnamed'
kolumny_do_wywalenia = [
    c
    for c in df.columns
    if c.lower() in ['id', 'column1'] or 'unnamed' in c.lower()
]
df_corr = df.drop(columns=kolumny_do_wywalenia, errors='ignore').select_dtypes(
    include=[np.number]
)

# Sprawdzenie w terminalu, czy diagnosis na pewno jest w danych
print(
    'Czy diagnosis jest w tabeli korelacji?:', 'diagnosis' in df_corr.columns
)

# 4. Obliczenie macierzy korelacji
corr_matrix = df_corr.corr()

# 5. Wykres z wyraźnymi cyframi
plt.figure(figsize=(26, 22))
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    vmin=-1,
    vmax=1,
    linewidths=0.5,
    linecolor='white',
    annot_kws={'size': 6.5},
    cbar_kws={'shrink': 0.8},
)

plt.title('Pełna macierz korelacji z kolumną diagnosis', fontsize=18, pad=20)
plt.xticks(rotation=90, fontsize=10)
plt.yticks(rotation=0, fontsize=10)
plt.tight_layout()
plt.show()
with pd.ExcelWriter('macierz_korelacji.xlsx') as writer:
    corr_matrix.to_excel(writer, sheet_name='Pelna_Macierz')
    if 'diagnosis' in corr_matrix.columns:
        ranking = corr_matrix[['diagnosis']].sort_values(
            by='diagnosis', ascending=False
        )
        ranking.to_excel(writer, sheet_name='Ranking_Wzgledem_Diagnosis')

corr_matrix.to_csv('macierz_korelacji.csv')
print(
)
plt.figure(figsize=(26, 22))
wybrana_paleta = 'magma'

sns.heatmap(
    corr_matrix,
    annot=True,
    fmt='.2f',
    cmap=wybrana_paleta,
    vmin=-1,
    vmax=1,
    linewidths=0.5,
    linecolor='#222222',
    annot_kws={'size': 6.5, 'weight': 'bold'},
    cbar_kws={'shrink': 0.8, 'label': 'Współczynnik korelacji'},
)

plt.title(
    f'Macierz korelacji cech (paleta: {wybrana_paleta})', fontsize=20, pad=20
)
plt.xticks(rotation=90, fontsize=10)
plt.yticks(rotation=0, fontsize=10)
plt.tight_layout()
plt.savefig('wykres_korelacji.png', dpi=300, bbox_inches='tight')
plt.show()