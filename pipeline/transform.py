import pandas as pd
from pipeline.extract import csv_para_df
from pipeline.logger import logger
from pathlib import Path


def renomea_colunas(caminho: Path) -> list:
    df: pd.DataFrame = csv_para_df(caminho)

    if df.empty():
        logger.erro(f"DataFrame vazio: {caminho.name}")
        raise ValueError(f"DataFrame vazio: {caminho.name}")

    colunas: list = df.columns

    nova_lista_colunas: list = list()
    for c in colunas:
        nome_coluna_tratado: str = c.lower().strip().replace(" ", "_")
        nova_lista_colunas.append(nome_coluna_tratado)

    return nova_lista_colunas


if __name__ == "__main__":
    try:
        path: Path = Path("data/raw/csat.csv")
        lista_de_colunas_renomeadas = renomea_colunas(path)
        print(lista_de_colunas_renomeadas)
    except Exception as err:
        print(err)
