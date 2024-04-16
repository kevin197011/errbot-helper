# Copyright (c) 2023 kk
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from dotenv import load_dotenv
from abc import ABC, abstractmethod


class BaseUtil(ABC):
    def __init__(self):
        load_dotenv()

    @abstractmethod
    def _instance(self):
        pass

    @abstractmethod
    def run(self):
        pass
