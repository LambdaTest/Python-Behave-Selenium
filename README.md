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
 behave
selenium
ConfigParser
```

## Test Scenario

### Single Test

In our demonstration, we will be creating a script that uses the Selenium WebDriver to click check boxes and add button. If assert returns true, it indicates that the test case passed successfully and will show up in the automation logs dashboard else if assert returns false, the test case fails, and the errors will be displayed in the automation logs.

You have successfully configured your project and are ready to execute your first pytest selenium testing script. Here is the  file for pytest selenium Testing which includes config.cfg fie. Lets call it <code>Steps_defination.py</code>.

```
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
    else:
        context.user_name = os.getenv('LT_USERNAME')
    if os.getenv('LT_ACCESS_KEY', 0)  == 0:
        context.app_key = config.get('Environment', 'AppKey' )
    else:
        context.app_key = os.getenv('LT_ACCESS_KEY')
    if os.getenv('LT_OPERATING_SYSTEM', 0) == 0:
        context.os = config.get('Environment', 'OS' )
    if os.getenv('LT_BROWSER', 0)  == 0:
        context.browser = config.get('Environment', 'Browser' )
    if os.getenv('LT_BROWSER_VERSION', 0)  == 0:
        context.browser_version = config.get('Environment', 'BrowserVersion' )

    remote_url= "https://"+context.user_name+":"+context.app_key+"@hub.lambdatest.com/wd/hub"
    caps['name'] = "LambdaTesBehaveSample"
    caps['build'] = "LambdaTestSampleApp"
    caps['browserName'] = context.browser       
    caps['version'] = context.browser_version
    caps['platform'] = context.os
    caps['network'] = True
    caps['visual']= True
    caps['video']= True
    caps['console']= True
    print ( caps )
    print ( remote_url )
    context.driver = webdriver.Remote(command_executor=remote_url,desired_capabilities=caps) 

@given('I go to 4davanceboy to add item')
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

#### To run file :

```
    $ behave features/lambdatest.feature
 ```

![behave](https://github.com/Apoorvlt/test/blob/master/behavecap.PNG)


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

