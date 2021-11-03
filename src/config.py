from dataset import Dataset
from typing import Dict

import toml


class ReaderConfig:
    def __init__(self, config_file = 'dataset_config.toml'):
        self.config_file = config_file
        self._data = {}

    @property
    def data(self) -> dict:
        return self._data

    def load(self, dt_section):
        self._data = Dataset(
            **toml.load(self.config_file).get("datasets").get(dt_section)
        )
        return self.data