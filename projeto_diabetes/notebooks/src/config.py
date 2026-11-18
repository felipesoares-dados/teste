from pathlib import Path

# Volta até 'projeto_diabetes' (parents[2]) e entra na subpasta 'projeto_teste'
PASTA_PROJETO = Path(__file__).resolve().parents[2] / "projeto_teste"

PASTA_DADOS = PASTA_PROJETO / "dados"

# coloque abaixo o caminho para os arquivos de dados de seu projeto
DADOS_ORIGINAIS = PASTA_DADOS / "diabetes.zip"
DADOS_TRATADOS = PASTA_DADOS / "diabetes_tratado.parquet"

# coloque abaixo outros caminhos que você julgar necessário
PASTA_RELATORIOS = PASTA_PROJETO / "relatorios"
PASTA_IMAGENS = PASTA_RELATORIOS / "imagens"