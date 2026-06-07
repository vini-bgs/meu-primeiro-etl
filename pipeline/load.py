from sqlalchemy import create_engine, URL
from dotenv import load_dotenv
from pipeline.logger import logger
import pandas as pd
import os


load_dotenv()

SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
DRIVER = os.getenv("DRIVER")
TABLE = os.getenv("TABLE")


def get_engine():
    try:
        connection_url = URL.create(
            drivername="mssql+pyodbc",
            host=SERVER,
            database=DATABASE,
            query={
                "driver": DRIVER,
                "Trusted_Connection": "yes",
            },
        )

    except Exception as err:
        logger.error(f"Atenção! {err}")
        raise

    return create_engine(connection_url, fast_executemany=True)


def load(df: pd.DataFrame) -> None:
    engine = None
    try:
        logger.info("Conectando ao banco...")
        engine = get_engine()
        logger.info("Conexão concluida!")
        df.to_sql(
            name=TABLE, con=engine, if_exists="append", index=False, chunksize=1000
        )
        logger.info(f"{len(df)} registros inseridos em '{TABLE}'.")

    except Exception as err:
        logger.error(f"Atenção! {err}")
        raise

    finally:
        if engine:
            engine.dispose()
            logger.info("Conexão encerrada.")


if __name__ == "__main__":
    from pathlib import Path
    from pipeline.extract import csv_para_df
    from pipeline.transform import (
        renomeia_colunas,
        trata_nulos,
        converte_tipos,
        validar_regras,
        conta_duplicatas,
    )

    path = Path("data/raw/csat.csv")
    df = csv_para_df(path)
    df = renomeia_colunas(df)
    df = trata_nulos(df)
    df = converte_tipos(df)
    df = validar_regras(df)
    df = conta_duplicatas(df)
    load(df)
