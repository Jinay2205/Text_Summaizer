import os
from box.exceptions import BoxValueError
from textsummarizer.logging import logger
from box import ConfigBox
from pathlib import Path
from ensure import ensure_annotations
import yaml
from typing import Any

@ensure_annotations 
def read_yaml(path_to_yaml:Path)->ConfigBox :
    try :
        with open(path_to_yaml) as file :
            content = yaml.safe_load(file)
            logger.info(f'{file} loaded')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('Yaml file empty')
    except Exception as e :
        raise e
    
@ensure_annotations
def create_dir(path_to_directories : list,verbose = True) : 
    for path in path_to_directories :
        os.makedirs(path,exist_ok=True) 
        if verbose :
            logger.info(f'created a directory at : {path}')

@ensure_annotations 
def get_size(path:Path)->str :
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'~ size in kb {size_in_kb}'
