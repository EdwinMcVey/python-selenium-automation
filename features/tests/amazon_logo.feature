# Created by Owner at 12/11/2021
Feature: Test Scenarios for findg Amazon logo

  Scenario: User can search for Amazon logo
    Given Open Amazon Create Account Page from Amazon Website
    When  Click on 'New Customer?'
    And   Create Account Page is present
    Then  Verify Amazon logo is present
