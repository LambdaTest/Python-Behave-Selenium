# Python-Behave-Selenium
![LambdaTest Logo](https://www.lambdatest.com/static/images/logo.svg)
---

![bh](https://github.com/Apoorvlt/test/blob/master/3344102.png)


## Prerequisites for Python Behave tutorial 

### 1. Python Installation

 * [Download Python](https://www.python.org/downloads/) and click on Add to path and install.
 
 * To check if python installed correctly you need to go to terminal type python in command prompt. It will show you the current version you have downloaded.
 
### 2. LambdaTest Credentials
  * To use Pytest with LambdaTest, make sure you have the 2 environment variables LT_USERNAME and LT_ACCESS_KEY set. To obtain a username and access_key, sign up for free [here](https://lambdatest.com). After signing up you can find your username and access key [here](https://accounts.lambdatest.com/detail/profile).
  * In the terminal export your LambdaTest Credentials as environmental variables:
       
       * For Mac/Linux
            ```
            $ export LT_USERNAME=<your LambdaTest username>
            $ export LT_ACCESS_KEY=<your LambdaTest access key>
            ```
       
       * For Windows
            ```
            set LT_USERNAME=<your LambdaTest username>
            set LT_ACCESS_KEY=<your LambdaTest access key>
    	       ```

### 3. Setup

 * Clone [Python-Behave-Selenium](https://github.com/LambdaTest/python-behave-selenium.git) from GitHub.
 * Navigate to the cloned directory
 * Install project dependencies by running command:
 
 ```
   pip install -r requirements.txt
 ```
 
 Requirements.txt file includes the following:
 
 ```
Paver==1.3.4
selenium==3.141.0
behave==1.2.6
```

## Test Scenario

### Single Test

In our demonstration, we will be creating a script that uses the Selenium WebDriver to click check boxes and add button. If assert returns true, it indicates that the test case passed successfully and will show up in the automation logs dashboard else if assert returns false, the test case fails, and the errors will be displayed in the automation logs.

You have successfully configured your project and are ready to execute your first pytest selenium testing script. Here is the  file for behave selenium Testing. Lets call it <code>config.cfg</code>.

```
[
    {
      "platform": "win10",
      "browserName": "chrome",
      "version": "76.0",
      "resolution": "1024x768",
      "name": "Behave Sample Test",
      "network": "true",
      "video": "true",
      "visual": "true",
      "console": "true"
    }
  ]
```

Here is <code>environment.py</code> file:

```
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
      
    
```

#### To run file  :

```
    $ behave features/lambdatest.feature
 ```

![behave](https://github.com/Apoorvlt/test/blob/master/behavecap.PNG)


### Parallel Testing

To run tests in parallel you need to set capaibilies and Update `config.json`  (List of supported OS platfrom, Browser, resolutions can be found at [LambdaTest capability generator](https://www.lambdatest.com/capabilities-generator/))
 example:

Setting capabilties for parallel execution
```
   [
     {
        "platform": "win10",
        "browserName": "chrome",
        "version": "67.0",
        "resolution": "1024x768",
        "name": "this is the behave test",
        "build": "behave-test-lambdatest"
     },
     {
        "platform": "win7",
        "browserName": "firefox",
        "version": "61.0",
        "resolution": "1024x768",
        "name": "this is the behave test",
        "build": "behave-test-lambdatest"
     }
   ]
   
```

```
* Note: Parallel is only working in windows due to paver library windows support issue.
```

Run test in parallel:

```
behave features/test.feature 

```

#### You can see these test log in our LambdaTest Automation page as well.

![](https://github.com/Apoorvlt/test/blob/master/cappal.PNG)


##  Routing traffic through your local machine using Lambdatest
- Set tunnel value to `True` in test capabilities
> OS specific instructions to download and setup tunnel binary can be found at the following links.
>    - [Windows](https://www.lambdatest.com/support/docs/display/TD/Local+Testing+For+Windows)
>    - [Mac](https://www.lambdatest.com/support/docs/display/TD/Local+Testing+For+MacOS)
>    - [Linux](https://www.lambdatest.com/support/docs/display/TD/Local+Testing+For+Linux)



Below we see a screenshot that depicts our Pytest code is running over different browsers i.e Chrome, Firefox and Safari on the LambdaTest Selenium Grid Platform. The results of the test script execution along with the logs can be accessed from the LambdaTest Automation dashboard.


![alttext](https://github.com/Apoorvlt/test/blob/master/Capture.PNG)



### Important Note:
---
- Some Safari & IE browsers, doesn't support automatic resolution of the URL string "localhost". Therefore if you test on URLs like "http://localhost/" or "http://localhost:8080" etc, you would get an error in these browsers. A possible solution is to use "localhost.lambdatest.com" or replace the string "localhost" with machine IP address. For example if you wanted to test "http://localhost/dashboard" or, and your machine IP is 192.168.2.6 you can instead test on "http://192.168.2.6/dashboard" or "http://localhost.lambdatest.com/dashboard".

## About LambdaTest
[LambdaTest](https://www.lambdatest.com/) is a cloud based selenium grid infrastructure that can help you run automated cross browser compatibility tests on 2000+ different browser and operating system environments. LambdaTest supports all programming languages and frameworks that are supported with Selenium, and have easy integrations with all popular CI/CD platforms. It's a perfect solution to bring your [selenium automation testing](https://www.lambdatest.com/selenium-automation) to cloud based infrastructure that not only helps you increase your test coverage over multiple desktop and mobile browsers, but also allows you to cut down your test execution time by running tests on parallel.

### Resources

##### [Selenium Documentation](http://www.seleniumhq.org/docs/)

##### [Python Documentation](https://docs.python.org/2.7/)

##### [Pytest Documentation](http://pytest.org/latest/contents.html)

