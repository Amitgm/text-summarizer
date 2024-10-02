
import os

from textsummarizer.logging import logger
from textsummarizer.entity import (DataValidationConfig)


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