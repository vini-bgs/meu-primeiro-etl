from loguru import logger
from pathlib import Path

Path("logs").mkdir(exist_ok=True)

logger.add(
    "logs/etl.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
),

logger.add(
    "logs/etl.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="ERROR",
),

logger.add(
    "logs/etl.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="WARNING",
)
