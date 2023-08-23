# Copyright (c) 2023 kk
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
import requests
from baseUtil import BaseUtil


class TGUtil(BaseUtil):
    def __init__(self):
        super().__init__()
        self.token = os.getenv("TELEGRAM_TOKEN")
        self.group_id = os.getenv("TELEGRAM_GROUP_ID")

    def _instance(self, msg) -> bool:
        _boolean = True
        data = {
            "chat_id": "123456789",
            "text": msg,
            "disable_notification": True,
        }
        response = requests.post(
            f"https://api.telegram.org/bot{self.token}/sendMessage", json=data
        )
        if response.status_code != 200:
            _boolean = False

        return _boolean

    def run(self, msg) -> bool:
        return self._instance(msg)
