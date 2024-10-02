from dataclasses import dataclass
from pathlib import Path
# import everything 
# note: here should be just from textsummarizer.constants import *, but we don't have that environment
from textsummarizer.utils.common import read_yaml, create_directories
import os
import urllib.request as request
import zipfile
from textsummarizer.logging import logger
from textsummarizer.utils.common import get_size

from textsummarizer.constants import *

# IMPORTANT TO CHANGE THE PATH WHEN creating directories for artefacts
# but running the code will be under research folder

os.chdir(r"C:\Users\Amit\MLops\text-summarizer")



# RETRUN TYPE OF THE FUNCTION, WHEN WRITING DATA INGESTION CONFIGURATION
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


class ConfigurationManager:

    #  because of from textsummarizer.constants import *
    def __init__(self,config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH ):

        self.config = read_yaml(config_filepath)    
        self.params = read_yaml(params_filepath)

        # this is how you can access the YAML files

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:

            config = self.config.data_ingestion

            # creating root directory for config.root_dir

            create_directories([config.root_dir])

            data_ingestion_config = DataIngestionConfig(

                root_dir = config.root_dir,
                source_URL = config.source_URL,
                local_data_file = config.local_data_file,
                unzip_dir = config.unzip_dir

            )

            return data_ingestion_config


class DataIngestion:

    def __init__(self,config:DataIngestionConfig):

        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):

            filename, headers = request.urlretrieve(

            url = self.config.source_URL,   
            filename = self.config.local_data_file

            )

            logger.info(f"{filename} download! with following info: \n{headers}")
        else:

            logger.info(f"file already exists {Path(self.config.local_data_file)}")

    def extract_zip_file(self):

        unzip_path = self.config.unzip_dir
        
        #  write exist_ok = True without needing to write if statement if path already exists
        os.makedirs(unzip_path,exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:

            zip_ref.extractall(unzip_path)


config = ConfigurationManager()

data_ingestion_config = config.get_data_ingestion_config()

data_ingestion = DataIngestion(config=data_ingestion_config)

data_ingestion.download_file()

data_ingestion.extract_zip_file()