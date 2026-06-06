import pandas as pd
from pathlib import Path
from pipeline.logger import logger


def csv_para_df(caminho_arquivo: Path) -> pd.DataFrame:
    """
    Função que lê um arquivo .csv e retorna um DataFrame
    """
    logger.info("Iniciando a extração...")
    if not caminho_arquivo.exists():
        logger.error(f"Arquivo não encontrado: {caminho_arquivo}")
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")

    df: pd.DataFrame = pd.read_csv(
        caminho_arquivo,
        sep=";",
        encoding="utf-8",
        dtype=str,
        low_memory=False,
        keep_default_na=False,
    )

    logger.info(f"{len(df)} linhas carregadas de '{caminho_arquivo.name}'")

    return df


if __name__ == "__main__":
    try:
        path: Path = Path("data/raw/filed.csv")
        print(csv_para_df(path))
    except Exception:
        print("err")
