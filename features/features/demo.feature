Feature: demo test, user navigates to google.com

  Background: maximize screen
    Given User maximize current window

  @demo
  Scenario: User navigates open browser and goes to google.com
    Given User navigates to "https://www.google.com/"
    When User enters "Python-automania GitHub" text in search box
    And User clicks search button
    Then User gets page title

  @demo2
  Scenario: User searchs on google and clicks on first link
    Given User navigates to "https://www.google.com/"
    When User enters "python automation github" text in search box
    And User clicks search button
    Then User clicks on first link
    And User gets page title