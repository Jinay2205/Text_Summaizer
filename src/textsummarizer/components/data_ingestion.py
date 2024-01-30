import os
import ssl
import logging
import zipfile
from pathlib import Path
from urllib import request
import certifi
from textsummarizer.entity import DataIngestionConfig
from textsummarizer.utils.common import get_size
logger = logging.getLogger(__name__)

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            # Create an SSL context with the certifi CA certificates
            ssl_context = ssl.create_default_context(cafile=certifi.where())
            try:
                # Use urlopen with the SSL context to download the file
                with request.urlopen(self.config.source_url, context=ssl_context) as response:
                    with open(self.config.local_data_file, 'wb') as file:
                        file.write(response.read())
                logger.info(f'{self.config.local_data_file} downloaded successfully')
            except Exception as e:
                logger.error(f'Error during file download: {e}')
                raise
        else:
            filename = self.config.local_data_file
            logger.info(f'{filename} already exists of size {get_size(Path(filename))}')

    def extract_zipfile(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as file:
            file.extractall(unzip_path)
        logger.info(f'ZIP file extracted to {unzip_path}')
