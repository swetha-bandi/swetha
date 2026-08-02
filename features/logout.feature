Feature: Logout functionality

  Scenario: logout with valid credentials

    Given user on login page
    When user enter the username "standard_user"
    And user enter the password "secret_sauce"
    And user click on login button
    And user click on burger button
    Then user click on logout button