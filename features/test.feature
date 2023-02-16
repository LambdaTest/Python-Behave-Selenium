Feature: Automate a website

    @Chrome
    Scenario: perform click events with Chrome
      When visit url "https://lambdatest.github.io/sample-todo-app"
      When check if title is "Sample page - lambdatest.com"
      When field with name "First Item" is present check the box
      When field with name "Second Item" is present check the box
      When select the textbox add "Let's add new to do item for chrome" in the box
      Then click the "addbutton"

    @Firefox
    Scenario: perform click events with Firefox
      When visit url "https://lambdatest.github.io/sample-todo-app"
      When check if title is "Sample page - lambdatest.com"
      When field with name "First Item" is present check the box
      When field with name "Second Item" is present check the box
      When select the textbox add "Let's add new to do item for Firefox" in the box
      Then click the "addbutton"

    @Edge
    Scenario: perform click events with Edge
      When visit url "https://lambdatest.github.io/sample-todo-app"
      When check if title is "Sample page - lambdatest.com"
      When field with name "First Item" is present check the box
      When field with name "Second Item" is present check the box
      When select the textbox add "Let's add new to do item for Edge" in the box
      Then click the "addbutton"