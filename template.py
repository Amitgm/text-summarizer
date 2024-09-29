import os
from pathlib import Path
#  to log information
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')


project_name = "textsummarizer"

list_of_files = [
    # automatic deployment of ci/cd pipeline, we wuse github, whenever a commit is pushed, it automatically take code from github and deloy it.
    ".github/workflows/.gitkeep",
    # when installing package,the init file will be needed
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    # all utils
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "reseach/trails.ipynb"
   ]

for filepath in list_of_files:

    filepath = Path(filepath)
    #  it splits the file path defined like config/config.yaml to config and config.yaml
    filedir,filename = os.path.split(filepath)


    #  some filedirs are not there in the list_of_files
    if filedir != "":
        
        #  if folder is present then ok, don't create folder if it already exists
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # if file doesn't exist or its size is 0, then create the file
    if not os.path.exists(filename) or (os.path.getsize(filename) == 0):

        with open(filepath,'w') as f:

            pass

            logging.info(f"Creating empty file: {filepath}")

    else:

           logging.info(f"file already exists: {filepath}")
        


