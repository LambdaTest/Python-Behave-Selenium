from behave.model_core import Status
from selenium import webdriver
import os
import json

INDEX = int(os.environ['INDEX']) if 'INDEX' in os.environ else 0
if os.environ.get("env") == "jenkins":
    desired_cap_dict = os.environ["LT_BROWSERS"]
    CONFIG = json.loads(desired_cap_dict)
else:
    json_file = "config/config.json"
    with open(json_file) as data_file:
        CONFIG = json.load(data_file)

username = os.environ["LT_USERNAME"]
authkey = os.environ["LT_ACCESS_KEY"]


def before_scenario(context, feature):
    desired_cap = setup_desired_cap(CONFIG[INDEX])
    if 'Chrome' in feature.tags:
        desired_cap["browserName"] = "chrome"
        desired_cap["platform"] = "Windows 11"
    elif 'Firefox' in feature.tags:
        desired_cap["browserName"] = "firefox"
        desired_cap["platform"] = "Windows 10"
    elif 'Edge' in feature.tags:
        desired_cap["browserName"] = "edge"
        desired_cap["platform"] = "Windows 8"

    print(str(desired_cap))
    context.browser = webdriver.Remote(
        desired_capabilities=desired_cap,
        command_executor="https://%s:%s@hub.lambdatest.com:443/wd/hub" % (username, authkey)
    )


def after_scenario(context, scenario):
    if scenario.status == Status.failed:
        context.browser.execute_script("lambda-status=failed")
    else:
        context.browser.execute_script("lambda-status=passed")
    context.browser.quit()


def setup_desired_cap(desired_cap):
    """
    sets the capability according to LT
    :param desired_cap:
    :return:
    """
    return desired_cap
