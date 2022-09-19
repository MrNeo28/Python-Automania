Feature: demo test browser

  Scenario: User navigates to google
    Given User navigates to "www.google.com"
    Then User gets page title
    When User enters "GitHub Behave" text in search box
    Then User gets page title