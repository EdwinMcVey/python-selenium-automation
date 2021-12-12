# Created by Owner at 12/11/2021
Feature: Test Scenarios for Cancelling Amazon Order

  Scenario: User can search for Cancelling an order
    Given Open Amazon Help page
    When  Click on Search Help Library
    And   Input Cancel order
    Then  Verify ‘Cancel Items or Orders’ text is present
