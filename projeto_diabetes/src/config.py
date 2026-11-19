"""Caminhos centralizados do projeto.

Todos os notebooks importam daqui os caminhos dos arquivos, evitando
caminhos escritos "na mão" e garantindo que o projeto rode em qualquer máquina.
"""

from pathlib import Path

# src/config.py -> parents[0] = src/ | parents[1] = raiz do projeto
PASTA_PROJETO = Path(__file__).resolve().parents[1]

# Dados
PASTA_DADOS = PASTA_PROJETO / "dados"
DADOS_ORIGINAIS = PASTA_DADOS / "diabetes.zip"  # CSV original compactado
DADOS_TRATADOS = PASTA_DADOS / "diabetes_tratado.parquet"  # gerado no notebook 01

# Relatórios (gráficos exportados usados no README)
PASTA_RELATORIOS = PASTA_PROJETO / "relatorios"
PASTA_IMAGENS = PASTA_RELATORIOS / "imagens"
