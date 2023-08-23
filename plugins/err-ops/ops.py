import re
from datetime import datetime
from errbot import BotPlugin, botcmd, re_botcmd
from jenkinsUtil import JenkinsUtil
from jiraUtil import JiraUtil


class Ops(BotPlugin):
    @botcmd(split_args_with=None)
    def tryops(self, msg, args):
        yield "tryops is ok! @{}".format(msg.frm._username)

    @botcmd(split_args_with=None)
    def jira(self, msg, args):
        _jira = JiraUtil()
        now = datetime.now().strftime("%Y%m%d")
        _jira.run(f"[devops] {now}更新", f"[devops] {now}更新")
        # print("jira issue created!")
        yield "kk devops jira issue created! @{}".format(msg.frm._username)

    # app
    @re_botcmd(pattern=r".*部署更新.*", prefixed=False, flags=re.DOTALL | re.IGNORECASE)
    def jenkins_deploy(self, msg, args):
        _status = None

        for line in str(msg).splitlines():
            if "name" in line:
                app_name = line.split(":")[1].strip().strip('"')
            if "env" in line:
                app_env = line.split(":")[1].strip()
            if "branch" in line:
                app_branch = line.split(":")[1].strip()

        yield "Jenkins job DEVOPS.001.deploy {app} {branch} {env} start deploying... @{user}".format(
            app=app_name, branch=app_branch, env=app_env, user=msg.frm._username
        )

        _status = JenkinsUtil().run(
            "DEVOPS.001.deploy",
            {
                "branch": app_branch,
                "env": app_env,
                "name": app_name,
            },
        )

        yield "Jenkins job DEVOPS.001.deploy {app} {branch} {env} deployed! [{build_id}]status: [{status}] @{user}".format(
            app=app_name,
            branch=app_branch,
            env=app_env,
            build_id=_status["job_id"],
            status=_status["job_status"].lower(),
            user=msg.frm._username,
        )
