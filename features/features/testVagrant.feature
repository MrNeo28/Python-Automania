Feature: User gets Country of Origin and Release Date

  Background: maximize screen
    Given User maximize current window

  @imdb
  Scenario Outline: : Imdb, Navigates
    Given User is on url 'https://www.imdb.com/'
    When User enters text '<MovieName>' on "imdb > searchBox"
    And User clicks on "imdb > searchButton"
    And User clicks on search result "imdb > searchResult"
    And User is on <MovieName> screen
    And User gets 'imdb > countryOfOrigin'
    And User gets 'imdb > releaseDate'

    Examples: |MovieName|
              |Pushpa: The Rise |
  @wiki
  Scenario Outline: : Wiki, Navigates
    Given User is on url 'https://en.wikipedia.org/'
    When User enters text '<MovieName>' on search box
    And User clicks on "searchButton"
    Then User is on search results screen
    And User clicks on search result
    And User is on <MovieName> screen
    And User gets country of origin
    And User gets release Date

    Examples: |MovieName|
              |Pushpa: The Rise |