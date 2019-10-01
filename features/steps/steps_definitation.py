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
      
    

