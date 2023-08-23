# Copyright (c) 2023 kk
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
import time
import jenkins
from baseUtil import BaseUtil


class JenkinsUtil(BaseUtil):
    def __init__(self):
        super().__init__()
        self.url = os.getenv("JENKINS_URL")
        self.username = os.getenv("JENKINS_USERNAME")
        self.password = os.getenv("JENKINS_PASSWORD")

    def _instance(self) -> jenkins.Jenkins:
        return jenkins.Jenkins(self.url, username=self.username, password=self.password)

    def run(self, job_name, job_params=None):
        msg = {"job_id": None, "job_status": None}
        try:
            _queue_id = self._instance().build_job(job_name, job_params)
            time.sleep(5)
            while True:
                _lastBuild_id = self._instance().get_job_info(job_name)["lastBuild"][
                    "number"
                ]
                _build_info = self._instance().get_build_info(job_name, _lastBuild_id)
                if _build_info["queueId"] != _queue_id:
                    continue
                time.sleep(2)
                if _build_info["result"] != None:
                    msg["job_id"] = _lastBuild_id
                    msg["job_status"] = _build_info["result"]
                    break
        except Exception as e:
            msg["job_status"] = str(e)
        return msg
