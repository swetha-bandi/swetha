Feature: Login functionality

  Scenario: login with valid credentials

    Given user on login page
    When user enter the username "standard_user"
    And user enter the password "secret_sauce"
    And user click on login button
    And user add back pack to add to cart
    And user clicks on the cart button
    And user clicks on checkout button
    And user enters firstname "swetha"
    And user enters lastname "bandi"
    And user enters postal code "123456"
    And user clicks continue button
    And user click finish button
    Then the order should be placed successfully
