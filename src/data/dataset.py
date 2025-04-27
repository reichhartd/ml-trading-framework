from os import makedirs


class Dataset:
    __PROCESSED_FOLDER = "data/processed/"
    __RAW_FOLDER = "data/processed/"
    __ZIP_FOLDER = "data/processed/"

    @staticmethod
    def __ensure_folders_exist():
        makedirs(Dataset.__PROCESSED_FOLDER, exist_ok=True)
        makedirs(Dataset.__RAW_FOLDER, exist_ok=True)
        makedirs(Dataset.__ZIP_FOLDER, exist_ok=True)
