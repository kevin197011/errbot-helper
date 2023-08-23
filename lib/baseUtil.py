# Copyright (c) 2023 kk
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from dotenv import load_dotenv


class BaseUtil:
    def __init__(self):
        load_dotenv()

    def _instance(self):
        pass

    def run(self):
        pass
