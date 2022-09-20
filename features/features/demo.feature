Feature: demo test browser

  Scenario: User navigates open browser and goes to google.com
    Given User navigates to "google"
    Then User gets page title
    When User enters "GitHub Behave" text in search box
    Then User gets page title