from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from pathlib import Path
from box.exceptions import BoxValueError
import os
import yaml


@ensure_annotations
def read_yaml_config(yaml_path: Path) -> ConfigBox:
    """
    Read and parse a YAML configuration file into a ConfigBox object.
    
    Args:
     yaml_path: Path to the YAML configuration file.
    
    Raises:
     ValueError: If the YAML file is empty.
     e: empty file
    
    Returns:
     ConfigBox: ConfigPath type
     
    """

    try:
        with open(yaml_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Successfully loaded configuration from {yaml_path}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"The YAML file at {yaml_path} is empty.")
    except Exception as e:
        raise e

@ensure_annotations
def create_directorys(directorys_path: list, verbose=True):
    """
    Create list of directorys.
    
    Args:
     directorys_path: List of directory paths.
        
    """
    for directory in directorys_path:
        os.makedirs(directory, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {directory}")

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_KB = round(os.path.getsize(path)/1024)
    return f"{size_in_KB} KB"
