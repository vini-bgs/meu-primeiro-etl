import pandas as pd
from pipeline.logger import logger
from pathlib import Path
from pipeline.extract import csv_para_df


def renomeia_colunas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Recebe um DataFrame e torna um DataFrame com as colunas tratadas:
    1. tudo minúsculo;
    2. sem espaços no começo ou fim;
    3. troca espaços no meio por "_"
    """
    try:
        df.columns = [c.lower().strip().replace(" ", "_") for c in df.columns]
        logger.info("Colunas verificadas...")
    except Exception as err:
        logger.error(f"Atenção! {err}")
        raise

    return df


def trata_nulos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Trata dados vazios das colunas 'city_name' e 'id_usurio'
    Além disso, retira o *.0 dos IDs
    """
    try:
        null_city = (df["city_name"] == "").sum()
        null_id_user = (df["id_usuario"] == "").sum()
        logger.info(f"Na coluna 'city_name' {null_city} valores são nulos")
        logger.info(f"Na coluna 'id_usuario' {null_id_user} valores são nulos")
        df["city_name"] = df["city_name"].replace("", "desconhecido")

        df["id_usuario"] = df["id_usuario"].str.split(".").str[0]
        df["id_usuario"] = df["id_usuario"].replace("", "desconhecido")

    except Exception as err:
        logger.error(f"Atenção! {err}")
        raise

    logger.info("Valores nulos tratados...")
    return df


if __name__ == "__main__":
    try:
        path: Path = Path("data/raw/csat.csv")
        df = csv_para_df(path)
        df_colunas_renomeadas = renomeia_colunas(df)
        df_final = trata_nulos(df_colunas_renomeadas)

    except Exception as err:
        print(err)
