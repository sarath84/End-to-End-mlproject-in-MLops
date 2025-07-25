import os
from src.exceptions import CustomException
from pathlib import Path
import sys
from box import ConfigBox as custombox
from src.logger import logging
import yaml
from typing import List
from ensure import ensure_annotations

@ensure_annotations
def read_yamls(config_file_path : Path)->custombox:
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
        with open(config_file_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {config_file_path} loaded successfully")
            return custombox(content)  

    except ValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise CustomException(e,sys)
    
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
            logging.info(f"created directory at: {path}")  


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
    