# here we are creating functions whenever we need to use it
import os
import yaml
from box.exceptions import BoxValueError
from textsummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

# config box is another way to access values in your dictionary  for example 
#  d1 = {"a": 1, "b": 2} here to access key a you use d1["a"] and not d1.a (which is convienient)
#  objectbox helps to access values with dot notation like d1.a where d1 = ConfigBox({"a": 1, "b": 2})


# ensure annotations helps to make sure the function parameters are of correct type
#  for example def add_numbers(a: int, b: int) -> int: , will work if a = 4 and b = 5 are integers and a = 4 and b = "5" where b is string
#  this is problematic if bymistake other data types are passed the output comes, ensure_annotations will help prevent this when placed above function
#  now when a = 4 and b = "5" where b is string is passed, it will raise value error annotation type error. so it's good practice to put ensure_annotations above the function.


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


