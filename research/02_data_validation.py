import os
os.chdir(r"C:\Users\Amit\MLops\text-summarizer")
# this goes into the entity folder
from dataclasses import dataclass
from pathlib import Path
from textsummarizer.constants import *
from textsummarizer.utils.common import read_yaml, create_directories
import urllib.request as request
import zipfile
from textsummarizer.logging import logger
from textsummarizer.utils.common import get_size

# RETRUN TYPE OF THE FUNCTION, WHEN WRITING DATA INGESTION CONFIGURATION
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE : str
    ALL_REQUIRED_FILES: list
# import everything 
# note: here should be just from textsummarizer.constants import *, but we don't have that environment


#  this goes into the configuration file under config folder
class ConfigurationManager:
    
    def __init__( self,config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH ):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # this is how you can access the YAML files

        create_directories([self.config.artifacts_root])


    def get_data_validation_config(self) -> DataValidationConfig:

            config = self.config.data_validation

            print(config)

            # creating root directory for config.root_dir

            create_directories([config.root_dir])

            data_validation_config = DataValidationConfig(

                root_dir = config.root_dir,
                STATUS_FILE = config.source_URL,
                ALL_REQUIRED_FILES = config.all_required_files
               

            )


            return data_validation_config


# this goes under components folder
class DataValidation:
    try:

        def __init__(self,config:DataValidationConfig):

            self.config = config

        def validate_all_file_exists(self) -> bool:

            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))

            for file in all_files:

                print("file",file)

                if file in self.config.ALL_REQUIRED_FILES:

                    status = True

                    with open(self.config.STATUS_FILE,'w') as f:

                        f.write(f"validation status { status}")

                        print(f"the file {file} exists")
                else:

                    status = False

                    with open(self.config.STATUS_FILE,'w') as f:

                        f.write(f"validation status { status}")

                        print(f"the file {file} does not exists")

            return status
        
    except Exception as e:

        raise e


#  this goes under the pipeline folder
config = ConfigurationManager()

data_validation_config = config.get_data_validation_config()

data_validation = DataValidation(config=data_validation_config)

data_validation.validate_all_file_exists()
