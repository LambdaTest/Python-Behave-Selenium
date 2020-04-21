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
        command_executor="https://%s:%s@hub.lambdatest.com:443/wd/hub" % (username, authkey)
    )


def after_feature(context, feature):
    context.browser.quit()


def setup_desired_cap(desired_cap):
    """
    sets the capability according to LT
    :param desired_cap:
    :return:
    """
    if os.environ.get('env') == 'jenkins':
        #sets the platform type
        desired_cap["platform"] = desired_cap["operatingSystem"]
        del desired_cap["operatingSystem"]
        #sets the browser version
        desired_cap["version"] = desired_cap["browserVersion"]
        del desired_cap["browserVersion"]
        #sets the tunnel name if configured
        if "LT_TUNNEL_NAME" in os.environ:
            desired_cap["TunnelName"] = os.environ["LT_TUNNEL_NAME"]
            desired_cap["tunnel"] = "true"
    if "tunnel" in desired_cap:
        if desired_cap["tunnel"].lower() == "true":
            desired_cap["tunnel"] = True
        elif desired_cap["tunnel"].lower() == "false":
            desired_cap["tunnel"] = False
    #shows the console logs in LT dashboard if set to true
    if "console" in desired_cap:
        if desired_cap["console"].lower() == "true":
            desired_cap["console"] = True
        elif desired_cap["console"].lower() == "false":
            desired_cap["console"] = False
    #shows the network logs in LT dashboard if set to true
    if "network" in desired_cap:
        if desired_cap["network"].lower() == "true":
            desired_cap["network"] = True
        elif desired_cap["network"].lower() == "false":
            desired_cap["network"] = False
    #shows the network logs in LT dashboard if set to true
    if "visual" in desired_cap:
        if desired_cap["visual"].lower() == "true":
            desired_cap["visual"] = True
        elif desired_cap["visual"].lower() == "false":
            desired_cap["visual"] = False
    # shows the video logs in LT dashboard if set to true
    if "video" in desired_cap:
        if desired_cap["video"].lower() == "true":
            desired_cap["video"] = True
        elif desired_cap["video"].lower() == "false":
            desired_cap["video"] = False
    return desired_cap