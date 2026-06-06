import pandas as pd
from pathlib import Path
from pipeline.logger import logger


path: Path = Path("data/raw/csat.csv")

if not path.exists():
    logger.error(f"Arquivo não encontrado: {path}")
    raise FileNotFoundError(f"Arquivo não encontrado: {path}")

df: pd.DataFrame = pd.read_csv(
    path,
    sep=";",
    encoding="utf-8",
    dtype=str,  # tipos de dados de cada coluna serão tratadps no transfor.py
    low_memory=False,
    keep_default_na=False,
)

logger.info(f"{len(df)} linhas carregadas de '{path.name}")
