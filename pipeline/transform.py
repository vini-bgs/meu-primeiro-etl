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


def converte_tipos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Define o tipo de cada coluna da tabela
    """
    try:
        logger.info("Convertendo tipos das colunas...")
        df["data_avaliacao"] = pd.to_datetime(df["data_avaliacao"], errors="coerce")
        df["frontline"] = pd.to_numeric(df["frontline"], errors="coerce")
        df["feedback"] = pd.to_numeric(df["feedback"], errors="coerce")
        df["star_4_5"] = pd.to_numeric(df["star_4_5"], errors="coerce")
        df["is_solved"] = pd.to_numeric(df["is_solved"], errors="coerce")
        df["star_num"] = pd.to_numeric(df["star_num"], errors="coerce").astype("Int64")
        df["id_usuario"] = df["id_usuario"].astype(str)

        logger.info("Colunas convertidas...")

    except Exception as err:
        logger.error(f"Atenção! {err}")
        raise

    return df


def validar_regras(df: pd.DataFrame) -> pd.DataFrame:
    """
    Verifica se existe algum valor na coluna star_4_5 (notas promotas)
    que estão com valores diferente de 0 e 1.
    Se tiver, apaga aquela linha.
    Além disso, informa se existe alguma linha com uma data futura
    """
    try:
        linhas_invalidas = (~df["star_4_5"].isin([0, 1])).sum()
        logger.warning(f"Foram encontradas {linhas_invalidas} linhas inválidas")
        logger.info(f"Excluindo {linhas_invalidas} linhas")
        df = df[df["star_4_5"].isin([0, 1])]
        logger.info("Linhas excluidas")

        data_minima = pd.Timestamp("2025-01-01")
        hoje = pd.Timestamp.today()
        datas_invalidas = (~df["data_avaliacao"].between(data_minima, hoje)).sum()
        logger.warning(f"Foram encontradas {datas_invalidas} datas inválidas")

    except Exception as err:
        logger.error(f"Atenção! {err}")
        raise

    return df


def conta_duplicatas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Verifica e loga a quantidade de tickets com mais de uma avaliação.
    """
    try:
        logger.info("Verificando duplicatas...")
        mask = df["origin_ticketid"].duplicated(keep=False)
        qtde_duplicatas = df[mask]["origin_ticketid"].nunique()
        logger.info(f"Foram encontrados {qtde_duplicatas} tickets duplicados")

    except Exception as err:
        logger.error(f"Atenção! {err}")
        raise

    return df


if __name__ == "__main__":
    try:
        path: Path = Path("data/raw/csat.csv")
        df = csv_para_df(path)
        df_colunas_renomeadas = renomeia_colunas(df)
        df_sem_nulo = trata_nulos(df_colunas_renomeadas)
        df_convertido = converte_tipos(df_sem_nulo)
        df_validado = validar_regras(df_convertido)
        df_sem_duplicatas = conta_duplicatas(df_validado)
        print(df_sem_duplicatas)

    except Exception as err:
        print(err)
