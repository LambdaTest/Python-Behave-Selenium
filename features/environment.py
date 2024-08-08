from behave.model_core import Status
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
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



def before_scenario(context, scenario):
    try:
        desired_cap = setup_desired_cap(CONFIG[INDEX])
        
        if 'Chrome' in scenario.tags:
            options = ChromeOptions()
            options.browser_version = desired_cap.get("version", "latest")
            options.platform_name = "Windows 11"
        elif 'Firefox' in scenario.tags:
            options = FirefoxOptions()
            options.browser_version = desired_cap.get("version", "latest")
            options.platform_name = "Windows 10"
        elif 'Edge' in scenario.tags:
            options = EdgeOptions()
            options.browser_version = desired_cap.get("version", "latest")
            options.platform_name = "Windows 8"
        else:
            raise ValueError("Unsupported browser tag")

        options.set_capability('build', desired_cap.get('build'))
        options.set_capability('name', desired_cap.get('name'))

        # Print options for debugging
        print("Browser Options:", options.to_capabilities())

        context.browser = webdriver.Remote(
            command_executor=f"https://{username}:{authkey}@hub.lambdatest.com/wd/hub",
            options=options
        )
    except Exception as e:
        print(f"Error in before_scenario: {str(e)}")
        context.scenario.skip(reason=f"Failed to initialize browser: {str(e)}")

def after_scenario(context, scenario):
    if hasattr(context, 'browser'):
        try:
            if scenario.status == Status.failed:
                context.browser.execute_script("lambda-status=failed")
            else:
                context.browser.execute_script("lambda-status=passed")
        except Exception as e:
            print(f"Error setting lambda status: {str(e)}")
        finally:
            context.browser.quit()


def setup_desired_cap(desired_cap):
    """
    Sets the capability according to LT
    :param desired_cap:
    :return:
    """
    # Create a new dictionary to avoid modifying the original
    cleaned_cap = {}
    
    for key, value in desired_cap.items():
        if key == 'connect':
            # Force 'connect' to be None if it's not a valid timeout value
            if not isinstance(value, (int, float)) or value is None:
                cleaned_cap[key] = None
            else:
                cleaned_cap[key] = value
        else:
            cleaned_cap[key] = value
    
    return cleaned_cap