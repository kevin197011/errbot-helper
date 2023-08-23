# Copyright (c) 2023 kk
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
from baseUtil import BaseUtil
from jira import JIRA
import os


class JiraUtil(BaseUtil):
    def __init__(self):
        super().__init__()
        self.server = os.getenv("JIRA_SERVER")
        self.username = os.getenv("JIRA_USERNAME")
        self.password = os.getenv("JIRA_PASSWORD")
        self.project = os.getenv("JIRA_PROJECT")

    def _instance(self):
        return JIRA(server=self.server, basic_auth=(self.username, self.password))

    def _create_issue(self, summary, description, issue_type="Task"):
        issue = self._instance().create_issue(
            project={"key": self.project},
            summary=summary,
            description=description,
            issuetype={"name": issue_type},
        )
        return issue

    def _assign_issue(self, issue, username):
        issue.update(assignee={"name": username})

    def run(self, summary, description, username="Kevin"):
        issue = self._create_issue(summary, description)
        self._assign_issue(issue, username)
