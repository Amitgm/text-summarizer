# this goes into the entity folder
from dataclasses import dataclass
from pathlib import Path

# RETRUN TYPE OF THE FUNCTION, WHEN WRITING DATA INGESTION CONFIGURATION
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path