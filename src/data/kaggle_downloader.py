import os
import shutil
import pandas as pd

from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile


class Dataset:
    """
    This class is a convenience wrapper for dataset functions. It taks care of interaction with the file system and downloading the dataset.

    """

    def __init__(self, test_mode=False):
        """
        constructor.
        If test_case is true, this will use different folders so unit tests don't interfere with any downloaded data.
        """

        self.DATASET_DIR_PATH = "data/raw/"
        self.ZIP_PATH = "data/zip/"
        self.ZIP_NAME = "bitcoin-historical-data.zip"

        if test_mode:
            self.DATASET_DIR_PATH = "tests/dataset/"
            self.ZIP_PATH = "tests/"

    def download(self) -> None:
        """download the dataset from Kaggle and unzip it to data/dataset"""

        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files("mczielinski/bitcoin-historical-data", path=self.ZIP_PATH)

        zip_file = ZipFile(self.ZIP_PATH + self.ZIP_NAME)
        zip_file = zip_file.extractall(path=self.DATASET_DIR_PATH)

        os.remove(self.ZIP_PATH + self.ZIP_NAME)

    def is_downloaded(self) -> bool:
        """checks if the data already has been downloaded"""

        return os.path.exists(self.DATASET_DIR_PATH + "data.csv")

    def remove_all(self) -> None:
        """removes all files associated with this dataset from the computer"""

        if os.path.exists(self.ZIP_PATH + self.ZIP_NAME):
            os.remove(self.ZIP_PATH + self.ZIP_NAME)
        if os.path.exists(self.DATASET_DIR_PATH):
            shutil.rmtree(self.DATASET_DIR_PATH)

    def get_original_data(self) -> pd.DataFrame:
        """
        Loads the original pokemon.csv as pandas self.
        If the dataset is not yet loaded, it will be loaded automatically.
        """

        if not self.is_downloaded():
            self.download()

        return pd.read_csv(self.DATASET_DIR_PATH + "data.csv")

