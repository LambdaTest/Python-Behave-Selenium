Feature: Automate a website
    Scenario: perform click events
      When visit url "https://lambdatest.github.io/sample-todo-app"
      When check if title is "Sample page - lambdatest.com"
      When field with name "First Item" is present check the box
      When field with name "Second Item" is present check the box
      When select the textbox add "Let's add new to do item" in the box
      Then click the "addbutton"