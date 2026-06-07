import pandas as pd
from pipeline.logger import logger
from pathlib import Path


def renomea_colunas(df: pd.DataFrame) -> pd.DataFrame:
    try:
        df.columns = [c.lower().strip().replace(" ", "_") for c in df.columns]
    except Exception as err:
        logger.error(f"Atenção! {err}")
        raise Exception((f"Atenção! {err}"))
    return df


if __name__ == "__main__":
    try:
        path: Path = Path("data/raw/csat.csv")
        lista_de_colunas_renomeadas = renomea_colunas(path)
        print(lista_de_colunas_renomeadas)
    except Exception as err:
        print(err)
