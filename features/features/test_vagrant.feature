Feature: User gets Country of Origin and Release Date

  Background: maximize screen
    Given User maximize current window

  @imdb
  Scenario Outline: Imdb, Navigates
    Given User is on url 'https://www.imdb.com/'
    When User enters text '<MovieName>' on 'imdb > searchBox'
    And User clicks on 'imdb > searchButton'
    And User pause for '3' s
    And User clicks on search result 'imdb > searchResult'
    And User is on '<MovieName>' screen
    And User gets 'imdb > countryOfOrigin' is 'India'
    And User gets 'imdb > releaseDate' on 'December 17, 2021'

    Examples: Name
              |MovieName|
              |Pushpa: The Rise |

  @wiki
  Scenario Outline: Wiki, Navigates
    Given User is on url 'https://en.wikipedia.org/'
    When User enters text '<MovieName>' on 'wiki > searchBox'
    And User clicks on 'wiki > searchButton'
    And User pause for '3' s
    And User clicks on search result 'wiki > searchResult'
    And User is on '<MovieName>' screen
    And User gets 'wiki > countryOfOrigin' is 'India'
    And User gets 'wiki > releaseDate' on '17 December 2021'

    Examples: Name movie
              |MovieName|
              |Pushpa: The Rise |