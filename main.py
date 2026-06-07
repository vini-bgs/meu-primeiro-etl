from pathlib import Path
from pipeline.logger import logger
from pipeline.extract import csv_para_df
from pipeline.load import load
from pipeline.transform import (
    renomeia_colunas,
    trata_nulos,
    converte_tipos,
    validar_regras,
    conta_duplicatas,
)

if __name__ == "__main__":

    try:
        logger.info(" === INICIANDO PIPELINE! === ")
        path = Path("data/raw/csat.csv")
        df = csv_para_df(path)
        df = renomeia_colunas(df)
        df = trata_nulos(df)
        df = converte_tipos(df)
        df = validar_regras(df)
        df = conta_duplicatas(df)
        load(df)
        logger.info(" === PIPELINE CONCLUÍDA! === ")

    except Exception as err:
        logger.error(f"Atenção! {err}")
        raise
