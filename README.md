![LambdaTest Logo](https://www.lambdatest.com/static/images/logo.svg)
---

# python-behave-todo
Behave integration with LambdaTest<br/>


### Setup
Install depedencies ```pip install -r requirements.txt```
### Configuration steps
##### Setting locally
- Set LambdaTest username and access key in environment variables. It can be obtained from [LambdaTest dashboard](https://automation.lambdatest.com/)
example:
- For linux/mac
```
   export LT_USERNAME="YOUR_USERNAME"
   export LT_ACCESS_KEY="YOUR ACCESS KEY"
  
```
- For Windows
```
   set LT_USERNAME="YOUR_USERNAME"
   set LT_ACCESS_KEY="YOUR ACCESS KEY"
  
```
 For setting capaibilies,Update `config.json`  (List of supported OS platfrom, Browser, resolutions can be found at [LambdaTest capability generator](https://www.lambdatest.com/capabilities-generator/))
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
*Note: Parallel is only working in windows due paver library windows support issue.

##### Setting test through jenkins
Please refer this [url](https://www.lambdatest.com/support/docs/display/TD/Selenium+with+Jenkins)
#####  Routing traffic through your local machine
- Set tunnel value to `true` in test capabilities
> OS specific instructions to download and setup tunnel binary can be found at the following links.
>    - [Windows](https://www.lambdatest.com/support/docs/display/TD/Local+Testing+For+Windows)
>    - [Mac](https://www.lambdatest.com/support/docs/display/TD/Local+Testing+For+MacOS)
>    - [Linux](https://www.lambdatest.com/support/docs/display/TD/Local+Testing+For+Linux)

### Run tests
##### Running tests through local (linux/unix)
```bash
paver run 
```
##### Running tests through local (windows)
```bash
behave features/lambdatest.feature 
```

##### Running tests through jenkins
```bash
paver run jenkins
```
## About LambdaTest

[LambdaTest](https://www.lambdatest.com/) is a cloud based selenium grid infrastructure that can help you run automated cross browser compatibility tests on 2000+ different browser and operating system environments. LambdaTest supports all programming languages and frameworks that are supported with Selenium, and have easy integrations with all popular CI/CD platforms. It's a perfect solution to bring your [selenium automation testing](https://www.lambdatest.com/selenium-automation) to cloud based infrastructure that not only helps you increase your test coverage over multiple desktop and mobile browsers, but also allows you to cut down your test execution time by running tests on parallel.
