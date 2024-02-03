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


def before_feature(context, feature):
    desired_cap = setup_desired_cap(CONFIG[INDEX])
    context.browser = webdriver.Remote(
        desired_capabilities=desired_cap,
        command_executor="https://%s:%s@hub.lambdatest.com/wd/hub" % (username, authkey)
    )


def after_feature(context, feature):
    context.browser.quit()


def setup_desired_cap(desired_cap):
    """
    sets the capability according to LT
    :param desired_cap:
    :return:
    """
    return desired_cap
