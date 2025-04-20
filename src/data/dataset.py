"""
This module provides functions to manage the complete dataset workflow.
"""

from .download_dataset import download_dataset
from .process_dataset import process_dataset


def prepare_dataset():
    """Prepare the dataset by downloading and processing it."""
    download_dataset()
    process_dataset()
