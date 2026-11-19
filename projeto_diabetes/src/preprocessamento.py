"""Engenharia de atributos para a modelagem preditiva (notebook 04).

Os modelos de classificação precisam de entradas numéricas. Como a base tratada
(notebook 01) tem colunas `category`, esta função converte tudo para inteiros
de forma determinística, sem "aprender" nada com os dados. Por isso ela pode ser
aplicada à base inteira antes da separação treino/teste sem causar vazamento
de dados (*data leakage*).
"""

import pandas as pd

COLUNA_ALVO = "Diabetes"


def codificar_atributos(dataframe, coluna_alvo=COLUNA_ALVO):
    """Separa os atributos (X) do alvo (y) e converte as categorias em inteiros.

    - Variável alvo: "Sim" vira 1 e "Não" vira 0.
    - Binárias (Não/Sim, Feminino/Masculino): 0 e 1, na ordem das categorias.
    - Ordinais (SaudeGeral, FaixaIdade, Ensino, FaixaRenda): código da categoria,
      que respeita a ordem natural definida no notebook 01 (0 = primeira categoria).
    - Numéricas (IMC e dias de problemas): mantidas como estão.

    Retorna a tupla (X, y).
    """
    y = (dataframe[coluna_alvo] == "Sim").astype("int8")
    X = dataframe.drop(columns=coluna_alvo).copy()

    for coluna in X.select_dtypes("category").columns:
        categorias = X[coluna].cat
        # Categorias sem ordem só são aceitas se forem binárias (0/1)
        if not categorias.ordered and len(categorias.categories) != 2:
            raise ValueError(f"A coluna {coluna!r} é categórica nominal com mais de 2 categorias.")
        if (categorias.codes < 0).any():
            raise ValueError(f"A coluna {coluna!r} tem valores ausentes.")
        X[coluna] = categorias.codes.astype("int8")

    return X, y
