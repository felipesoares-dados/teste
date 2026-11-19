"""Funções estatísticas de apoio usadas no notebook 02.

Cada função de teste recebe um DataFrame em que cada coluna é um grupo
(por exemplo, uma coluna para quem tem diabetes e outra para quem não tem),
executa o teste e imprime a conclusão com base no nível de significância `alfa`.
"""

from scipy.stats import (
    levene,
    mannwhitneyu,
    ttest_ind,
)


def analise_levene(dataframe, alfa=0.05, centro="mean"):
    """Teste de Levene: verifica se as variâncias dos grupos (colunas) são iguais.

    H0: as variâncias são iguais. `centro` pode ser "mean", "median" ou "trimmed";
    "median" é mais robusto para dados assimétricos.
    """
    print("Teste de Levene")
    
    estatistica_levene, valor_p_levene = levene(
        *[dataframe[coluna] for coluna in dataframe.columns], 
        center=centro, 
        nan_policy="omit"
    )
        
    print(f"{estatistica_levene=:.3f}")
    if valor_p_levene > alfa:
        print(f"Variâncias iguais (valor p: {valor_p_levene:.3f})")
    else:
        print(f"Ao menos uma variância é diferente (valor p: {valor_p_levene:.3f})")


def analise_mannwhitneyu(
    dataframe,
    alfa=0.05,
    alternativa="two-sided",
):
    """Teste de Mann-Whitney U: compara dois grupos sem exigir normalidade.

    H0: as distribuições dos dois grupos são iguais.
    """

    print("Teste de Mann-Whitney")
    estatistica_mw, valor_p_mw = mannwhitneyu(
        *[dataframe[coluna] for coluna in dataframe.columns],
        nan_policy="omit",
        alternative=alternativa,
    )

    print(f"{estatistica_mw=:.3f}")
    if valor_p_mw > alfa:
        print(f"Não rejeita a hipótese nula (valor p: {valor_p_mw:.3f})")
    else:
        print(f"Rejeita a hipótese nula (valor p: {valor_p_mw:.3f})")


def analise_ttest_ind(
    dataframe,
    alfa=0.05,
    variancias_iguais=True,
    alternativa="two-sided",
):
    """Teste t para duas amostras independentes (Student ou Welch).

    H0: as médias dos dois grupos são iguais. Use `variancias_iguais=False`
    para o teste de Welch, quando o Levene indicar variâncias diferentes.
    """
    print("Teste t de Student")
    estatistica_ttest, valor_p_ttest = ttest_ind(
        *[dataframe[coluna] for coluna in dataframe.columns], 
        equal_var=variancias_iguais,
        alternative=alternativa,
        nan_policy="omit"
    )
        
    print(f"{estatistica_ttest=:.3f}")
    if valor_p_ttest > alfa:
        print(f"Não rejeita a hipótese nula (valor p: {valor_p_ttest:.3f})")
    else:
        print(f"Rejeita a hipótese nula (valor p: {valor_p_ttest:.3f})")


def remove_outliers(dados, largura_bigodes=1.5):
    """
    Remove outliers de um array de dados baseado no método do boxplot.
    
    Parâmetros:
    - dados: array-like, os dados dos quais remover os outliers.
    - largura_bigodes: float, o fator multiplicativo para o IQR (Interquartile Range).
    
    Retorna:
    - dados_sem_outliers: array-like, os dados sem os outliers.
    """
    q1 = dados.quantile(0.25)
    q3 = dados.quantile(0.75)
    iqr = q3 - q1

    return dados[(dados >= q1 - (largura_bigodes * iqr)) & (dados <= q3 + (largura_bigodes * iqr))]
