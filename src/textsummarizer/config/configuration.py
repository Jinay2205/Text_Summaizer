from textsummarizer.constants import *
from textsummarizer.utils.common import read_yaml,create_dir
from textsummarizer.entity import DataIngestionConfig,DataValidationConfig

class ConfigurationManager :
    def __init__(self,config_path = CONFIGURE_FILE_PATH,param_path = PARAM_FILE_PATH):

        self.config = read_yaml(config_path)
        self.param = read_yaml(param_path)
        create_dir([self.config.artifacts_root])

    def get_ingestion_config(self)->DataIngestionConfig :
        config = self.config.data_ingestion
        create_dir([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    def get_validation_config(self)->DataValidationConfig :
        config = self.config.data_validation
        create_dir([config.root_dir])
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )
        return data_validation_config