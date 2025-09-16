# Importando bibliotecas.
import pandas as pd
import numpy as np


# Criando DataFrame para exemplo.
dados = {
    'Produto': ['Teclado', 'Mouse', 'Monitor', 'CPU', 'Webcam'],
    'Preço': [150.0, 75.0, 800.0, np.nan, 250.0], # Gerando valores vazios com o numpy (np.nan)
    'Estoque': [30, 45, 12, 5, np.nan]
}


# DataFrame com pandas
df = pd.DataFrame(dados)


# Criando variável que recebe a média dos valores na coluna 'Preço'.
media_preco = df['Preço'].mean()


# Preenchendo espaço vazio com variável de média criada usando metódo .fillna().
df['Preço'] = df['Preço'].fillna(media_preco)


# Criando variável que recebe a mediana da coluna 'Estoque'.
mediana_estoque = df['Estoque'].median()


# Preenchendo espaço vazio com variável de mediana criada usando metódo .fillna().
df['Estoque'] = df['Estoque'].fillna(mediana_estoque)


# Resultado Final
print('=== \033[1mDados Preenchidos\033[0m ===\n')
print(df)