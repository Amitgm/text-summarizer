# import everything 
# note: here should be just from textsummarizer.constants import *, but we don't have that environment
from textsummarizer.constants import *
from textsummarizer.utils.common import read_yaml, create_directories
from textsummarizer.entity import (DataIngestionConfig)

class ConfigurationManager:
    def __init__( self,config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH ):

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


        
