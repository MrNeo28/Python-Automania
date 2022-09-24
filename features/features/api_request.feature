Feature: User send request and get response

    Background: Create a presistent session
        When User creates a session 
    
    @demo_api
    Scenario: User send login request and gets status code  200
        When User send request to "https://reqres.in/api/login"
        And User enter login creds
        Then User assert status code equals 200