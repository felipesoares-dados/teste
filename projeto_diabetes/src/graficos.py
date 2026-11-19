"""Arquivo de construção de gráficos para distribuições de probabilidade.
Construído para o módulo de Estatística do curso de Ciência de Dados ministrado
por Francisco Bustamante.

Pode ser modificado e distribuído livremente, desde que mantida a referência ao autor
a partir deste comentário de cabeçalho.

Autor: Francisco Bustamante
https://www.linkedin.com/in/flsbustamante
"""

import math

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter


def plotar_histogramas_preenchidos(
    data,
    colunas,
    coluna_alvo,
    titulo="Distribuição por variável",
    ncols=1,
    nrows=None,
    figsize=None,
    labelrotation=0,
):
  """Gráficos de barras 100% empilhadas: proporção de `coluna_alvo` em cada categoria.

  Parâmetros:
  - data: DataFrame com os dados.
  - colunas: lista de colunas categóricas, uma por gráfico.
  - coluna_alvo: coluna usada como cor (hue), por exemplo "Diabetes".
  - titulo: título geral da figura.
  - ncols / nrows: grade de gráficos (nrows é calculado se omitido).
  - figsize: tamanho da figura; se omitido, é ajustado ao número de gráficos.
  - labelrotation: rotação, em graus, dos rótulos do eixo x.
  """
  total_graficos = len(colunas)

  if nrows is None:
    nrows = math.ceil(total_graficos / ncols)

  # Ajusta o tamanho da figura proporcionalmente ao número de linhas/colunas
  if figsize is None:
    largura = 12 if ncols == 1 else ncols * 3.5
    altura = nrows * 3.8
    figsize = (largura, altura)

  fig, axs = plt.subplots(
      nrows=nrows, ncols=ncols, figsize=figsize, sharey=True
  )

  if hasattr(axs, "flat"):
    axs_flat = list(axs.flat)
  elif isinstance(axs, (list, tuple)):
    axs_flat = list(axs)
  else:
    axs_flat = [axs]

  handles, labels = [], []

  for i, coluna in enumerate(colunas):
    ax = axs_flat[i]
    h = sns.histplot(
        data=data,
        x=coluna,
        hue=coluna_alvo,
        multiple="fill",
        ax=ax,
        stat="percent",
        shrink=0.8,
    )

    ax.tick_params(axis="x", labelrotation=labelrotation)
    ax.yaxis.set_major_formatter(PercentFormatter(1))
    ax.set_ylabel("")
    ax.set_title(coluna, fontsize=12, fontweight="bold", pad=8)
    ax.set_xlabel("")

    for barra in h.containers:
      h.bar_label(
          barra,
          label_type="center",
          labels=[f"{parte.get_height():.1%}" for parte in barra],
          color="white",
          weight="bold",
      )

    legend = h.get_legend()
    if legend:
      handles = legend.legend_handles
      labels = [text.get_text() for text in legend.get_texts()]
      legend.remove()

  for j in range(total_graficos, len(axs_flat)):
    fig.delaxes(axs_flat[j])

  # TÍTULO E LEGENDA GLOBAIS
  fig.suptitle(titulo, fontsize=16, fontweight="bold", y=0.98)

  if handles and labels:
    fig.legend(
        handles=handles,
        labels=labels,
        loc="upper center",
        ncols=len(labels),
        title=coluna_alvo,
        bbox_to_anchor=(0.5, 0.94),
    )

  # Ajusta o layout deixando 15% de margem no topo reservada para a legenda e título
  plt.tight_layout(rect=[0, 0, 1, 0.86])
  plt.show()
