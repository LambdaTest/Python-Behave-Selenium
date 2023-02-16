# Run Selenium Tests With Behave On LambdaTest

![171934563-4806efd2-1154-494c-a01d-1def95657383 (1)](https://user-images.githubusercontent.com/70570645/172273386-fa9606ac-3e63-4b2e-8978-3142add3e038.png)

<p align="center">
  <a href="https://www.lambdatest.com/blog/?utm_source=github&utm_medium=repo&utm_campaign=python-behave-selenium" target="_bank">Blog</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/support/docs/?utm_source=github&utm_medium=repo&utm_campaign=python-behave-selenium" target="_bank">Docs</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/learning-hub/?utm_source=github&utm_medium=repo&utm_campaign=python-behave-selenium" target="_bank">Learning Hub</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/newsletter/?utm_source=github&utm_medium=repo&utm_campaign=python-behave-selenium" target="_bank">Newsletter</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/certifications/?utm_source=github&utm_medium=repo&utm_campaign=python-behave-selenium" target="_bank">Certifications</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.youtube.com/c/LambdaTest" target="_bank">YouTube</a>
</p>
&emsp;
&emsp;
&emsp;

*Learn how to run your Python automation testing scripts using Behave on the LambdaTest platform*

[<img height="58" width="200" src="https://user-images.githubusercontent.com/70570645/171866795-52c11b49-0728-4229-b073-4b704209ddde.png">](https://accounts.lambdatest.com/register)


## Table Of Contents

* [Pre-requisites](#pre-requisites)
* [Run Your First Test](#run-your-first-test)
* [Local Testing With Behave](#testing-locally-hosted-or-privately-hosted-projects)

## Prerequisites For Running Robot Selenium Tests
* * *
Before you can start performing Python automation testing using Robot, you would need to:

* Install the latest Python build from the [official website](https://www.python.org/downloads/). We recommend using the latest version i.e python 3.
* Make sure **pip 3** is installed in your system. You can install **pip** from [here](https://pip.pypa.io/en/stable/installation/).
* Download the latest **Selenium Client** and its **WebDriver bindings** from the [official website](https://www.selenium.dev/downloads/). Latest versions of **Selenium Client** and **WebDriver** are ideal for running your automation script on LambdaTest Selenium cloud grid.
* Install **virtualenv** which is the recommended way to run your tests. It will isolate the build from other setups you may have running and ensure that the tests run with the specified versions of the modules.
```bash
pip install virtualenv
```
### Installing Selenium Dependencies And Tutorial Repo

**Step 1:** Clone the LambdaTest’s Python-Behave-Selenium repository and navigate to the code directory as shown below:

```bash
git clone https://github.com/LambdaTest/Python-Behave-Selenium
cd Python-Behave-Selenium
```

**Step 2:** Create a virtual environment in your project folder the environment name is arbitrary.

```bash
virtualenv venv
```

**Step 3:** Activate the environment.

```bash
source venv/bin/activate
```

**Step 4:** Install the [required packages](https://github.com/LambdaTest/Python-Behave-Selenium/blob/master/requirements.txt) from the cloned project directory:

```bash
pip install -r requirements.txt
```
### Setting Up Your Authentication

Make sure you have your LambdaTest credentials with you to run test automation scripts. You can get these credentials from the [LambdaTest Automation Dashboard](https://automation.lambdatest.com/build) or by your [LambdaTest Profile](https://accounts.lambdatest.com/login).

**Step 5:** Set LambdaTest **Username** and **Access Key** in environment variables.

* For **Linux/macOS**:
  
  ```bash
  export LT_USERNAME="YOUR_USERNAME" 
  export LT_ACCESS_KEY="YOUR ACCESS KEY"
  ```
  * For **Windows**:
  ```bash
  set LT_USERNAME="YOUR_USERNAME" 
  set LT_ACCESS_KEY="YOUR ACCESS KEY"
  ```


## Run Your First Test

>**Test Scenario**: The below Python Behave script tests a simple to-do application with basic functionalities like mark items as done, add items in list, calculate total pending items etc.

```python
from selenium import webdriver
import os
from configparser import ConfigParser
 
caps={}
 
def before_all(context):   
    config = ConfigParser()
    print ((os.path.join(os.getcwd(), 'config.cfg')))
    my_file = (os.path.join(os.getcwd(), 'config.cfg'))
    config.read(my_file)
     
    if os.getenv('LT_USERNAME', 0) == 0:
        context.user_name = config.get('Environment', 'UserName')
    if os.getenv('LT_ACCESS_KEY', 0)  == 0:
        context.access_key = config.get('Environment', 'AccessKey' )
    if os.getenv('LT_OPERATING_SYSTEM', 0) == 0:
        context.os = config.get('Environment', 'OS' )
    if os.getenv('LT_BROWSER', 0)  == 0:
        context.browser = config.get('Environment', 'Browser' )
    if os.getenv('LT_BROWSER_VERSION', 0)  == 0:
        context.browser_version = config.get('Environment', 'BrowserVersion' )
 
    remote_url= "https://"+context.user_name+":"+context.app_key+"@hub.lambdatest.com/wd/hub"
    caps['name'] = "Behave Sample Test"
    caps['build'] = "Behave Selenium Sample"
    caps['browserName'] = context.browser      
    caps['version'] = context.browser_version
    print ( caps )
    print ( remote_url )
    context.driver = webdriver.Remote(command_executor=remote_url,desired_capabilities=caps)
 
@given('I go to sample-todo-app to add item')
def step(context):
    before_all(context)
    context.driver.get('https://lambdatest.github.io/sample-todo-app/')
 
@then('I Click on first checkbox and second checkbox')
def click_on_checkbox_one(context):
    context.driver.find_element_by_name('li1').click()
    context.driver.find_element_by_name('li2').click()
 
@when('I enter item to add')
def enter_item_name(context):
    context.driver.find_element_by_id('sampletodotext').send_keys("Yey, Let's add it to list")
 
@when('I click add button')
def click_on_add_button(context):
    context.driver.find_element_by_id('addbutton').click()
 
@then('I should verify the added item')
def see_login_message(context):
    context.driver.implicitly_wait(10)
    added_item = context.driver.find_element_by_xpath("//span[@class='done-false']").text
    print(added_item)
    print(added_item)
    if added_item in "Yey, Let's add it to list":
        return True
    else:
        return False
 
def after_all(context):
    context.browser.quit()
```
### Configuration Of Your Test Capabilities

**Step 6:** In `config/config.json`, you need to update your test capabilities. In this code, we are passing browser, browser version, and operating system information, along with LambdaTest Selenium grid capabilities via capabilities object. The capabilities object in the above code are defined as:
```python
[
    {
      "platform": "Windows 10",
      "browserName": "chrome",
      "version": "latest",
      "build": "Behave Selenium Sample",
      "name": "Behave Sample Test"
    }
  ]
```
> You can generate capabilities for your test requirements with the help of [Desired Capability Generator](https://www.lambdatest.com/capabilities-generator/).

### Executing The Test

**Step 7:** The tests can be executed in the terminal using the following command.
```bash
behave features/test.feature 
```

**Step 8:** The tests can be executed in the terminal parallel using behavex via tags.
```bash
behavex -t @Firefox,@Chrome,@Edge --parallel-processes 3 
```
Your test results would be displayed on the test console (or command-line interface if you are using terminal/cmd) and on LambdaTest automation dashboard. [LambdaTest Automation Dashboard](https://automation.lambdatest.com/build) will help you view all your text logs, screenshots and video recording for your entire automation tests.

## Testing Locally Hosted or Privately Hosted Projects
***
You can test your locally hosted or privately hosted projects with [LambdaTest Selenium grid cloud](https://www.lambdatest.com/selenium-automation) using LambdaTest Tunnel app. All you would have to do is set up an SSH tunnel using LambdaTest Tunnel app and pass toggle `tunnel = True` via desired capabilities. LambdaTest Tunnel establishes a secure SSH protocol based tunnel that allows you in testing your locally hosted or privately hosted pages, even before they are made live.

>Refer our [LambdaTest Tunnel documentation](https://www.lambdatest.com/support/docs/testing-locally-hosted-pages/) for more information.

Here’s how you can establish LambdaTest Tunnel.

Download the binary file of:

* [LambdaTest Tunnel for Windows](https://downloads.lambdatest.com/tunnel/v3/windows/64bit/LT_Windows.zip)
* [LambdaTest Tunnel for Mac](https://downloads.lambdatest.com/tunnel/v3/mac/64bit/LT_Mac.zip)
* [LambdaTest Tunnel for Linux](https://downloads.lambdatest.com/tunnel/v3/linux/64bit/LT_Linux.zip)

Open command prompt and navigate to the binary folder.

Run the following command:
```bash
LT -user {user’s login email} -key {user’s access key}
```
So if your user name is lambdatest@example.com and key is 123456, the command would be:
```bash
LT -user lambdatest@example.com -key 123456
```
Once you are able to connect **LambdaTest Tunnel** successfully, you would just have to pass on tunnel capabilities in the code shown below :

**Tunnel Capability**

```bash
"tunnel" : true
```

## Documentation & Resources :books:

      
Visit the following links to learn more about LambdaTest's features, setup and tutorials around test automation, mobile app testing, responsive testing, and manual testing.

* [LambdaTest Documentation](https://www.lambdatest.com/support/docs/?utm_source=github&utm_medium=repo&utm_campaign=python-behave-selenium)
* [LambdaTest Blog](https://www.lambdatest.com/blog/?utm_source=github&utm_medium=repo&utm_campaign=python-behave-selenium)
* [LambdaTest Learning Hub](https://www.lambdatest.com/learning-hub/?utm_source=github&utm_medium=repo&utm_campaign=python-behave-selenium)    

## LambdaTest Community :busts_in_silhouette:

The [LambdaTest Community](https://community.lambdatest.com/) allows people to interact with tech enthusiasts. Connect, ask questions, and learn from tech-savvy people. Discuss best practises in web development, testing, and DevOps with professionals from across the globe 🌎

## What's New At LambdaTest ❓

To stay updated with the latest features and product add-ons, visit [Changelog](https://changelog.lambdatest.com/) 
      
## About LambdaTest

[LambdaTest](https://www.lambdatest.com) is a leading test execution and orchestration platform that is fast, reliable, scalable, and secure. It allows users to run both manual and automated testing of web and mobile apps across 3000+ different browsers, operating systems, and real device combinations. Using LambdaTest, businesses can ensure quicker developer feedback and hence achieve faster go to market. Over 500 enterprises and 1 Million + users across 130+ countries rely on LambdaTest for their testing needs.    

### Features

* Run Selenium, Cypress, Puppeteer, Playwright, and Appium automation tests across 3000+ real desktop and mobile environments.
* Real-time cross browser testing on 3000+ environments.
* Test on Real device cloud
* Blazing fast test automation with HyperExecute
* Accelerate testing, shorten job times and get faster feedback on code changes with Test At Scale.
* Smart Visual Regression Testing on cloud
* 120+ third-party integrations with your favorite tool for CI/CD, Project Management, Codeless Automation, and more.
* Automated Screenshot testing across multiple browsers in a single click.
* Local testing of web and mobile apps.
* Online Accessibility Testing across 3000+ desktop and mobile browsers, browser versions, and operating systems.
* Geolocation testing of web and mobile apps across 53+ countries.
* LT Browser - for responsive testing across 50+ pre-installed mobile, tablets, desktop, and laptop viewports

    
[<img height="58" width="200" src="https://user-images.githubusercontent.com/70570645/171866795-52c11b49-0728-4229-b073-4b704209ddde.png">](https://accounts.lambdatest.com/register)


      
## We are here to help you :headphones:

* Got a query? we are available 24x7 to help. [Contact Us](support@lambdatest.com)
* For more info, visit - [LambdaTest](https://www.lambdatest.com/?utm_source=github&utm_medium=repo&utm_campaign=python-behave-selenium)
